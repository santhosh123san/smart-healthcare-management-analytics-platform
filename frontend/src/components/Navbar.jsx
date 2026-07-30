import "./Navbar.css";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        Smart Healthcare
      </div>

      <ul className="navbar-links">
        <li>
          <Link to="/">Dashboard</Link>
        </li>

        <li>
          <Link to="/patients">Patients</Link>
        </li>

        <li>
          <span>Doctors</span>
        </li>

        <li>
          <span>Appointments</span>
        </li>

        <li>
          <span>Analytics</span>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;