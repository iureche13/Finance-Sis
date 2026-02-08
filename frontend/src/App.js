import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";

function IntakeForm() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Intake Form</h1>
      <button onClick={() => navigate("/homepage")}>
        Submit Form
      </button>
    </div>
  );
}

function ResultsPage() {
  return <h1>Results Page</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<IntakeForm />} />
        <Route path="/results" element={<ResultsPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
