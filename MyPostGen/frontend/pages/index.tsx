import { useState } from "react";

export default function Home() {
  const [domain, setDomain] = useState("AI/ML/GenAI/RAG (default)");
  const [idea, setIdea] = useState("");
  const [post, setPost] = useState("");

  const handleGenerate = async () => {
    const res = await fetch("railwaydeployedpythonserver-production.up.railway.app", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_idea: idea, domain }),
    });
    const data = await res.json();
    setPost(data.post);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>🤖 AI-Generated LinkedIn Post</h1>
      <label>Domain:</label>
      <select value={domain} onChange={(e) => setDomain(e.target.value)}>
        <option>AI/ML/GenAI/RAG (default)</option>
        <option>Data Science & Analytics</option>
        <option>Agentic AI</option>
        <option>SaaS</option>
        <option>Healthcare AI</option>
        <option>Custom</option>
      </select>
      <br /><br />
      <label>Your Input (optional):</label><br />
      <textarea rows={4} value={idea} onChange={(e) => setIdea(e.target.value)} />
      <br /><br />
      <button onClick={handleGenerate}>🚀 Generate Post</button>
      <br /><br />
      {post && (
        <>
          <h3>✅ Your LinkedIn Post:</h3>
          <textarea rows={15} value={post} readOnly style={{ width: "100%" }} />
        </>
      )}
    </div>
  );
}
