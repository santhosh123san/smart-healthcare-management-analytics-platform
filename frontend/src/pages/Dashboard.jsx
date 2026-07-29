import "../styles/Dashboard.css";

 function Dashboard() {
  return (
    <div className="dashboard">
      <h1>Hospital Dashboard</h1>

      <p>
        Welcome to the Smart Healthcare Management & Analytics Platform.
      </p>

      <div className="kpi-container">
        <div className="kpi-card">
          <h3>Total Patients</h3>
          <p>1,250</p>
        </div>

        <div className="kpi-card">
          <h3>Doctors</h3>
          <p>85</p>
        </div>

        <div className="kpi-card">
          <h3>Appointments Today</h3>
          <p>142</p>
        </div>

        <div className="kpi-card">
          <h3>Available Beds</h3>
          <p>48</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;