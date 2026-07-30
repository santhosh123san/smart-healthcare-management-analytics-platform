import "./Sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">
      <h3>Hospital Menu</h3>

      <ul>
        <li>Dashboard</li>
        <li>Patients</li>
        <li>Doctors</li>
        <li>Appointments</li>
        <li>Billing</li>
        <li>Laboratory</li>
        <li>Pharmacy</li>
        <li>Analytics</li>
        <li>Reports</li>
      </ul>
    </aside>
  );
}

export default Sidebar;