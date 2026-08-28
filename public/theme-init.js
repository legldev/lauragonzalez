try {
  const savedTheme = localStorage.getItem('laura-theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const useDarkTheme = savedTheme === 'dark' || (!savedTheme && prefersDark);
  document.documentElement.classList.toggle('dark', useDarkTheme);
  document.getElementById('theme-color')?.setAttribute('content', useDarkTheme ? '#100810' : '#fff6f4');
} catch {
  // The light theme remains the safe default when browser storage is unavailable.
}
