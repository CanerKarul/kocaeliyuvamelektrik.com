document.addEventListener('DOMContentLoaded',function(){
  const toggle=document.querySelector('[data-menu-toggle]');
  const menu=document.querySelector('[data-mobile-menu]');
  if(toggle&&menu){toggle.addEventListener('click',function(){let v=menu.classList.toggle('is-open');toggle.setAttribute('aria-expanded',String(v));});menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{menu.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');}));}
  const input=document.querySelector('[data-service-filter]');
  if(input){const cards=[...document.querySelectorAll('[data-service-search]')];const empty=document.querySelector('[data-no-results]');input.addEventListener('input',function(){const q=(input.value||'').toLocaleLowerCase('tr-TR').trim();let visible=0;cards.forEach(c=>{const show=c.dataset.serviceSearch.toLocaleLowerCase('tr-TR').includes(q);c.hidden=!show;if(show)visible++;});if(empty)empty.style.display=visible?'none':'block';});}
});
