const express = require('express');
const router = express.Router();

// Get revenue overview
router.get('/overview', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const stats = orchestrator.getStats();
    
    res.json({
      success: true,
      data: {
        totalRevenue: stats.revenue,
        monthlyRecurring: 85000,
        projectedAnnual: 9500000,
        revenueStreams: {
          consultations: 250000,
          courses: 120000,
          memberships: 85000,
          affiliates: 45000
        },
        growth: {
          daily: '+$5,000',
          weekly: '+$35,000',
          monthly: '+$150,000',
          percentage: '+30%'
        }
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Generate revenue
router.post('/generate', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const result = await orchestrator.executeWorkflow('revenue-generation', req.body);
    
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Get revenue forecast
router.get('/forecast', async (req, res) => {
  try {
    const orchestrator = req.app.locals.orchestrator;
    const analyticsAgent = orchestrator.agents.get('analytics');
    
    const predictions = await analyticsAgent.instance.execute('predictTrends', {});
    
    res.json({
      success: true,
      data: {
        nextMonth: predictions.predictions.nextMonth.revenue,
        nextQuarter: predictions.predictions.nextQuarter.revenue,
        nextYear: predictions.predictions.nextYear.revenue,
        confidence: predictions.predictions.nextMonth.confidence
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

module.exports = router;
