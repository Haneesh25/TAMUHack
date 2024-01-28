// AutomatedResourceAllocation.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AutomatedResourceAllocation.css'; // Import a CSS file for custom styles

const AutomatedResourceAllocation = () => {
    // ... useState and useEffect logic remain the same

    return ( <
        div className = "widget-container" >
        <
        h3 className = "widget-title" > Resource Allocation Advice < /h3> <
        div className = "advice-container" >
        <
        p > { allocationData.advice } < /p> <
        /div> <
        div className = "stats-container" >
        <
        p > < strong > Current Check - In Counters: < /strong> {allocationData.stats.checkInCounters}</p >
        <
        p > < strong > Currently Open Counters: < /strong> {allocationData.stats.openCounters}</p >
        <
        p > < strong > Predicted Queue Time: < /strong> {allocationData.stats.predictedQueueTime}</p >
        <
        /div> <
        /div>
    );
};