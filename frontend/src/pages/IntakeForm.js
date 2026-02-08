import { useNavigate } from "react-router-dom";

function IntakeForm() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Intake Form</h1>
      <button onClick={() => navigate("/results")}>
        Submit Form
      </button>
    </div>
  );
}
export default IntakeForm