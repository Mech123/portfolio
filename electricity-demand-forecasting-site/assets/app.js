(function () {
  const year = document.getElementById("year");
  const githubLink = document.getElementById("githubLink");

  if (year) year.textContent = new Date().getFullYear();

  if (githubLink) {
    githubLink.href = "https://github.com/Mech123/dswp_group2/tree/main";
  }
})();
