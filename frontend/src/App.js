import { BrowserRouter, Routes, Route } from "react-router-dom";
import IntakeForm from "./pages/FrontPage/IntakeForm";
import ResultsPage from "./pages/ResultsPage/ResultsPage";

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
