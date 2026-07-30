function Doctors() {
  return (
    <div className="dashboard">
      <h1>Doctors</h1>

      <p>
        Manage and monitor doctor information.
      </p>

      <div className="kpi-container">
        <div className="kpi-card">
          <h3>Total Doctors</h3>
          <p>85</p>
        </div>

        <div className="kpi-card">
          <h3>Available Today</h3>
          <p>62</p>
        </div>

        <div className="kpi-card">
          <h3>On Leave</h3>
          <p>8</p>
        </div>

        <div className="kpi-card">
          <h3>Departments</h3>
          <p>12</p>
        </div>
      </div>
    </div>
  );
}

export default Doctors;