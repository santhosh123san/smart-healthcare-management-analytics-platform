function Patients() {
  return (
    <div className="dashboard">
      <h1>Patients</h1>

      <p>
        Manage and monitor patient information.
      </p>

      <div className="kpi-container">
        <div className="kpi-card">
          <h3>Total Patients</h3>
          <p>1,250</p>
        </div>

        <div className="kpi-card">
          <h3>New Patients</h3>
          <p>45</p>
        </div>

        <div className="kpi-card">
          <h3>Active Patients</h3>
          <p>1,120</p>
        </div>

        <div className="kpi-card">
          <h3>Discharged</h3>
          <p>85</p>
        </div>
      </div>
    </div>
  );
}

export default Patients;