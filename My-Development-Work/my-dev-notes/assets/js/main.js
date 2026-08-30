document.addEventListener('DOMContentLoaded', () => {
  // Mobile sidebar toggle
  const sidebar = document.getElementById('sidebar');
  const backdrop = document.getElementById('backdrop');
  const menuToggle = document.getElementById('menuToggle');
  function closeMenu() {
    sidebar && sidebar.classList.remove('open');
    backdrop && backdrop.classList.remove('open');
  }
  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      backdrop.classList.toggle('open');
    });
  }
  if (backdrop) backdrop.addEventListener('click', closeMenu);

  // Theme toggle (persists for the session)
  const themeToggle = document.getElementById('themeToggle');
  const html = document.documentElement;
  const savedTheme = sessionStorage.getItem('theme');
  if (savedTheme) html.dataset.theme = savedTheme;
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      html.dataset.theme = html.dataset.theme === 'dark' ? 'light' : 'dark';
      sessionStorage.setItem('theme', html.dataset.theme);
    });
  }

  // TOC scroll spy
  const tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length) {
    const targets = Array.from(tocLinks)
      .map((a) => document.getElementById(a.getAttribute('href').slice(1)))
      .filter(Boolean);
    window.addEventListener('scroll', () => {
      let current = targets[0];
      targets.forEach((sec) => {
        if (sec && window.scrollY >= sec.offsetTop - 100) current = sec;
      });
      tocLinks.forEach((a) => a.classList.remove('active'));
      if (current) {
        const match = document.querySelector('.toc a[href="#' + current.id + '"]');
        if (match) match.classList.add('active');
      }
    });
  }

  // Ctrl+K search demo
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      alert('Search is a static demo in this project — wire up a real search later if you want.');
    }
  });
  const searchBox = document.querySelector('.search-box');
  if (searchBox) {
    searchBox.addEventListener('click', () => {
      alert('Search is a static demo in this project — wire up a real search later if you want.');
    });
  }
});

document.querySelectorAll(".quiz-question").forEach(function(question){

  const options = question.querySelectorAll(".quiz-option");
  const correctAnswer = question.dataset.answer;
  const result = question.querySelector(".quiz-result");

  options.forEach(function(option){

    option.addEventListener("click", function(){

      if(question.classList.contains("answered")){
        return;
      }

      question.classList.add("answered");

      const selectedAnswer = option.textContent.trim().charAt(0);

      options.forEach(function(btn){
        btn.disabled = true;
      });

      if(selectedAnswer === correctAnswer){

        option.classList.add("correct");

        result.innerHTML =
          "✓ Correct! Well done.";

        result.classList.add("correct-result");

      }else{

        option.classList.add("incorrect");

        options.forEach(function(btn){

          const answer = btn.textContent.trim().charAt(0);

          if(answer === correctAnswer){
            btn.classList.add("correct");
          }

        });

        result.innerHTML =
          "✗ Incorrect. The correct answer is <strong>" +
          correctAnswer +
          "</strong>.";

        result.classList.add("incorrect-result");
      }

    });

  });

});