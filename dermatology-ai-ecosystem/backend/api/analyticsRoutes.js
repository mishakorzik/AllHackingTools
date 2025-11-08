const express = require('express');
const router = express.Router();

// Get dashboard analytics
router.get('/dashboard', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const stats = orchestrator.getStats();
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const performance = await analyticsAgent.instance.execute('trackPerformance', {});
    const insights = await analyticsAgent.instance.execute('generateInsights', {});
    
    res.json({
      success: true,
      data: {
        overview: {
          activeAgents: stats.activeAgents,
          tasksProcessed: stats.totalTasksProcessed,
          revenue: stats.revenue,
          successRate: stats.successRate
        },
        performance: performance.performance,
        insights: insights.insights.slice(0, 5),
        timestamp: new Date().toISOString()
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Get quality metrics
router.get('/quality', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const qualityControl = await analyticsAgent.instance.execute('qualityControl', { workflows: {} });
    
    res.json({
      success: true,
      data: qualityControl
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Get optimization recommendations
router.get('/optimize', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const optimizations = await analyticsAgent.instance.execute('optimizeWorkflows', {});
    
    res.json({
      success: true,
      data: optimizations
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

module.exports = router;
