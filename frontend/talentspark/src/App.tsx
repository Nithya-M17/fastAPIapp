import Welcome from "./components/welcome";
import NavBar from "./components/NavBar";
import CompanyCard from "./components/CompanyCard";
import JobCard from "./components/JobCard";
import Footer from "./components/Footer";
import { useEffect, useState } from "react";

import {
  getCompanies,
  createCompany,
  updateCompany,
  deleteCompany,
} from "./Services/CompanyService";

import type { Company } from "./types/company";

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [companies, setCompanies] = useState<Company[]>([]);

  async function fetchCompanies() {
    setLoading(true);

    try {
      const data = await getCompanies();
      setCompanies(data);
    } catch (error) {
      setError(error as Error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchCompanies();
  }, []);

  async function handleAdd(company: Company) {
    await createCompany(company);
    await fetchCompanies();
  }

  async function handleEdit(company: Company) {
    await updateCompany(company.id, company);
    await fetchCompanies();
  }

  async function handleDelete(id: number) {
    await deleteCompany(id);
    await fetchCompanies();
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      <NavBar />
      <Welcome />

      <br />

      <CompanyCard
        companies={companies}
        onadd={handleAdd}
        onedit={handleEdit}
        ondelete={handleDelete}
      />

      <JobCard />

      <Footer />
    </>
  );
}

export default App;