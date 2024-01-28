import React from 'react';
import { Map, TileLayer, HeatmapLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const HeatmapVisualization = ({ data }) => {
    return ( <
        Map center = {
            [airportLat, airportLng] }
        zoom = { 15 } >
        <
        TileLayer url = "" /
        >
        <
        HeatmapLayer fitBoundsOnLoad fitBoundsOnUpdate points = { data }
        longitudeExtractor = { m => m[1] }
        latitudeExtractor = { m => m[0] }
        intensityExtractor = { m => parseFloat(m[2]) }
        /> <
        /Map>
    );
};