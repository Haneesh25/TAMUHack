// Dashboard.js

import React from 'react';
import PredictiveAnalyticsWidget from '../PredictiveAnalyticsWidget';
import AutomatedResourceAllocation from './AutomatedResourceAllocation';
import './Dashboard.css'; // Import a CSS file for custom dashboard styles, if needed

const Dashboard = () => {
    return ( <
        div className = "dashboard-container" >
        <
        PredictiveAnalyticsWidget / >
        <
        AutomatedResourceAllocation / > { /* Additional components or widgets can be added here */ } <
        /div>
    );
};

export default Dashboard;