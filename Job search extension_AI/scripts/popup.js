
document.getElementById("startButton").addEventListener("click", () => {
    const resumeInput = document.getElementById("resumeInput");
    if (resumeInput.files.length === 0) {
        document.getElementById("status").textContent = "Please upload a resume.";
        return;
    }
    document.getElementById("status").textContent = "Processing your resume...";
    // Simulate resume parsing and job fetching
    setTimeout(() => {
        document.getElementById("status").textContent = "Jobs matched and applications sent!";
    }, 2000);
});
