const express = require('express');
const router = express.Router();

// Get all agents status
router.get('/status', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const stats = orchestrator.getStats();
    
    res.json({
      success: true,
      data: {
        activeAgents: stats.activeAgents,
        totalTasksProcessed: stats.totalTasksProcessed,
        successRate: stats.successRate,
        revenue: stats.revenue,
        agentBreakdown: {
          content: 8000,
          marketing: 7000,
          patientCare: 6000,
          sales: 5000,
          analytics: 4000,
          brand: 3000,
          education: 3000,
          support: 2000,
          research: 1500,
          qualityControl: 500
        }
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Execute workflow
router.post('/workflow', async (req, res) => {
  try {
    const { workflowType, params } = req.body;
    const orchestrator = req.app.locals.orchestrator;
    
    const result = await orchestrator.executeWorkflow(workflowType, params || {});
    
    res.json({
      success: true,
      workflow: workflowType,
      result
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Get agent performance
router.get('/performance', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const performance = await analyticsAgent.instance.execute('trackPerformance', {});
    
    res.json({
      success: true,
      data: performance
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Get insights
router.get('/insights', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const insights = await analyticsAgent.instance.execute('generateInsights', {});
    
    res.json({
      success: true,
      data: insights
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Get predictions
router.get('/predictions', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const predictions = await analyticsAgent.instance.execute('predictTrends', {});
    
    res.json({
      success: true,
      data: predictions
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

module.exports = router;
