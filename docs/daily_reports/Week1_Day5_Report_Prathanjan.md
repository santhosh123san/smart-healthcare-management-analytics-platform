# Week 1 Day 5 Report – Prathanjan

## 1. Objective

To introduce the Patients page and implement frontend routing so users can navigate between the Dashboard and Patients modules.

## 2. Tasks Completed

- Created the Patients page.
- Added sample patient KPI information.
- Installed React Router.
- Added BrowserRouter, Routes, and Route configuration.
- Created Dashboard and Patients routes.
- Added clickable Dashboard and Patients links to the Sidebar.
- Added clickable Dashboard and Patients links to the Navbar.
- Tested navigation between Dashboard and Patients.
- Verified the Patients page using the /patients route.
- Updated the Files Created Log.
- Updated the Development Log.
- Captured the Day 5 Patients page screenshot.

## 3. Files Created

- frontend/src/pages/Patients.jsx
- docs/daily_reports/Week1_Day5_Report_Prathanjan.md
- screenshots/week1/day5/Week1_Day5_Patients_Page.png

## 4. Files Modified

- frontend/src/App.jsx
- frontend/src/components/Sidebar.jsx
- frontend/src/components/Navbar.jsx
- frontend/package.json
- frontend/package-lock.json
- docs/project_management/Development_Log.txt
- docs/project_management/Files_Created_Log.txt

## 5. Dependency Added

- react-router-dom

## 6. Frontend Progress

The application now supports separate Dashboard and Patients pages using React Router. Navigation is available through both the Sidebar and Navbar.

## 7. Testing

The following navigation was successfully tested:

- Dashboard → /
- Patients → /patients
- Sidebar navigation
- Navbar navigation

## 8. Challenges Faced

The frontend initially had no routing mechanism for multiple pages.

## 9. Solution Implemented

React Router was installed and configured using BrowserRouter, Routes, Route, and Link components.

## 10. Outcome

Successfully implemented the Patients page and basic application routing, creating a foundation for additional healthcare modules.

## 11. Next Plan

- Continue developing healthcare application modules.
- Improve page structure and reusable components.
- Prepare the frontend for backend/API integration.
- Continue maintaining project documentation and logs.