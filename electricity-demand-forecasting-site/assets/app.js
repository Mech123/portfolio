(function(){
  const sidebar = document.getElementById("sidebar");
  const menuBtn = document.getElementById("menuBtn");
  const year = document.getElementById("year");
  const githubLink = document.getElementById("githubLink");
  const screencastLink = document.getElementById("screencastLink");
  const screencastWrap = document.getElementById("screencastWrap");

  if (year) year.textContent = new Date().getFullYear();

  // Update links here
  const LINKS = {
    github: "https://github.com/Mech123/dswp_group2/tree/main",
    screencast: "" // none for now
  };

  if (githubLink) githubLink.href = LINKS.github;

  // Hide screencast button if empty
  if (!LINKS.screencast) {
    if (screencastWrap) screencastWrap.style.display = "none";
  } else {
    if (screencastLink) screencastLink.href = LINKS.screencast;
  }

  function toggleSidebar(){
    const isMobile = window.matchMedia("(max-width: 980px)").matches;
    if (!isMobile) return;

    if (sidebar.classList.contains("open")){
      sidebar.classList.remove("open");
      sidebar.classList.add("closed");
    } else {
      sidebar.classList.remove("closed");
      sidebar.classList.add("open");
    }
  }

  if (menuBtn) menuBtn.addEventListener("click", toggleSidebar);

  document.querySelectorAll(".nav-link").forEach(a => {
    a.addEventListener("click", () => {
      const isMobile = window.matchMedia("(max-width: 980px)").matches;
      if (isMobile){
        sidebar.classList.remove("open");
        sidebar.classList.add("closed");
      }
    });
  });

  const isMobile = window.matchMedia("(max-width: 980px)").matches;
  if (isMobile && sidebar){
    sidebar.classList.add("closed");
  }
})();
