import "../styles/Dashboard.css";
import KpiCard from "../components/KpiCard";

function Dashboard() {
  return (
    <div className="dashboard">
      <h1>Hospital Dashboard</h1>

      <p>
        Welcome to the Smart Healthcare Management & Analytics Platform.
      </p>

      <div className="kpi-container">
        <KpiCard title="Total Patients" value="1,250" />
        <KpiCard title="Doctors" value="85" />
        <KpiCard title="Appointments Today" value="142" />
        <KpiCard title="Available Beds" value="48" />
      </div>
    </div>
  );
}

export default Dashboard;