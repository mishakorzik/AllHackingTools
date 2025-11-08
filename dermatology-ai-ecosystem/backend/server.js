const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const { createServer } = require('http');
const { Server } = require('socket.io');
const winston = require('winston');

// Import routes
const agentRoutes = require('./api/agentRoutes');
const revenueRoutes = require('./api/revenueRoutes');
const analyticsRoutes = require('./api/analyticsRoutes');

// Import orchestration
const AgentOrchestrator = require('./orchestration/AgentOrchestrator');

dotenv.config();

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: process.env.FRONTEND_URL || 'http://localhost:3000',
    methods: ['GET', 'POST']
  }
});

// Logger setup
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
    new winston.transports.Console({ format: winston.format.simple() })
  ]
});

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Request logging
app.use((req, res, next) => {
  logger.info(`${req.method} ${req.path}`);
  next();
});

// Initialize Agent Orchestrator
const orchestrator = new AgentOrchestrator(io, logger);

// Make orchestrator available to routes
app.locals.orchestrator = orchestrator;
app.locals.logger = logger;

// Routes
app.use('/api/agents', agentRoutes);
app.use('/api/revenue', revenueRoutes);
app.use('/api/analytics', analyticsRoutes);

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    activeAgents: orchestrator.getActiveAgentCount(),
    totalTasks: orchestrator.getTotalTasksProcessed()
  });
});

// WebSocket connection for real-time updates
io.on('connection', (socket) => {
  logger.info(`Client connected: ${socket.id}`);
  
  socket.on('disconnect', () => {
    logger.info(`Client disconnected: ${socket.id}`);
  });
  
  socket.on('startAgentWorkflow', async (data) => {
    try {
      const result = await orchestrator.executeWorkflow(data.workflowType, data.params);
      socket.emit('workflowComplete', result);
    } catch (error) {
      socket.emit('workflowError', { error: error.message });
    }
  });
});

// Error handling
app.use((err, req, res, next) => {
  logger.error(err.stack);
  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong'
  });
});

const PORT = process.env.PORT || 5000;

httpServer.listen(PORT, () => {
  logger.info(`🚀 Dermatology AI Ecosystem Server running on port ${PORT}`);
  logger.info(`📊 Dashboard: http://localhost:${PORT}`);
  logger.info(`🤖 Initializing 40,000 virtual employees...`);
  orchestrator.initialize();
});

module.exports = { app, httpServer };
