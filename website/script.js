
//Menu Toggle

function toggleMenu() {
    const menu = document.querySelector('.menu-links')
    const icon = document.querySelector('.hamburger-icon')
    menu.classList.toggle("open")
    icon.classList.toggle("open")
}



// === Visitor Counter Logic ===

// Load API configuration
async function loadConfig() {
  try {
    const res = await fetch("/config.json", { cache: "no-store" });
    if (!res.ok) throw new Error("Failed to load config.json");
    return await res.json();
  } catch (err) {
    console.error("Config load error:", err);
    return null;
  }
}

// Fetch visitor count from API
async function getVisitorCount() {
  const cfg = await loadConfig();
  if (!cfg) {
    document.getElementById("visitor-count").textContent =
      "Error loading configuration.";
    return;
  }

  const apiUrl = `${cfg.API_BASE}`;
  console.log(apiUrl)

  try {
    const res = await fetch(apiUrl, { method: "GET" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    const count = data.count ?? data.visitorCount ?? 0; // support variations
    const div = document.getElementById("visitor-count");
    div.textContent = `👋 ${count.toLocaleString()} visitors so far!`;
  } catch (err) {
    console.error("Error fetching visitor count:", err);
    document.getElementById("visitor-count").textContent =
      "Oops… can’t count you right now!";
  }
}

// Run visitor count fetch when the page loads
document.addEventListener("DOMContentLoaded", getVisitorCount);
