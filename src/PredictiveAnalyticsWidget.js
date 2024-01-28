// PredictiveAnalyticsWidget.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import './PredictiveAnalyticsWidget.css'; // Import a CSS file for custom styles

const PredictiveAnalyticsWidget = () => {
    // ... useState and useEffect logic remain the same

    return ( <
        div className = "widget-container" >
        <
        h3 className = "widget-title" > Passenger Flow Forecast < /h3> <
        div className = "chart-container" >
        <
        ResponsiveContainer width = "100%"
        height = { 300 } >
        <
        BarChart data = { forecastData } >
        <
        CartesianGrid strokeDasharray = "3 3" / >
        <
        XAxis dataKey = "time" / >
        <
        YAxis / >
        <
        Tooltip / >
        <
        Legend / >
        <
        Bar dataKey = "passengerCount"
        fill = "#82ca9d"
        barSize = { 30 }
        /> <
        /BarChart> <
        /ResponsiveContainer> <
        /div> <
        /div>
    );
};