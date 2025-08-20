document.getElementById("gradeEssay").addEventListener("click", async () => {
    const essayText = document.getElementById("essayInput").value;
    if (!essayText.trim()) {
        alert("Please enter an essay.");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/submit-essay/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: essayText }),
        });

        const data = await response.json();
        document.getElementById("originalityScore").textContent = data.feedback.originality + "/100";
        document.getElementById("readabilityScore").textContent = data.feedback.readability + "/100";
        document.getElementById("relevanceScore").textContent = data.feedback.relevance + "/100";
        document.getElementById("grammarScore").textContent = data.feedback.grammar_coherence + "/100";
    } catch (error) {
        alert("Error fetching grading results.");
    }
});
