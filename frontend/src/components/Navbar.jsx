import "./Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        Smart Healthcare
      </div>

      <ul className="navbar-links">
        <li>
          <a href="/">Dashboard</a>
        </li>

        <li>
          <a href="/">Patients</a>
        </li>

        <li>
          <a href="/">Doctors</a>
        </li>

        <li>
          <a href="/">Appointments</a>
        </li>

        <li>
          <a href="/">Analytics</a>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;