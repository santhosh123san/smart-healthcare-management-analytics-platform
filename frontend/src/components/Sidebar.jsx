import "./Sidebar.css";
import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <aside className="sidebar">
      <h3>Hospital Menu</h3>

      <ul>
        <li>
          <Link to="/">Dashboard</Link>
        </li>

        <li>
          <Link to="/patients">Patients</Link>
        </li>

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