/**
 * ACSOFT - ALTERNATIVE CREATIVE SOFTWARE STUDIOS
 * Script Oficial de Interatividade, Animações e Sistema do Usuário
 * Contato Oficial: +55 74 991969827 | eukaioluccas31@gmail.com
 * Fundadores: Júlia Almeida Costa (Júlia A.R) & Kaio Lucas Celestino Da Silva Reis (Kaio Lucas A.R)
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initFoundersInteractive();
  initColorPaletteCopier();
  initServicesFilter();
  initProjectCalculator();
  initFaqAccordion();
  initContactForm();
  initScrollAnimations();
});

/* ==========================================================================
   1. NAVEGAÇÃO & HEADER SCROLL
   ========================================================================== */
function initNavbar() {
  const header = document.getElementById('header');
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  // Efeito de shrink & blur ao rolar
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    updateActiveNavLink();
  }, { passive: true });

  // Menu Mobile Drawer
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      document.body.style.overflow = !isExpanded ? 'hidden' : '';
    });

    // Fechar ao clicar em links
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileToggle.classList.remove('active');
        navMenu.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Fechar ao clicar fora
    document.addEventListener('click', (e) => {
      if (!header.contains(e.target) && navMenu.classList.contains('active')) {
        mobileToggle.classList.remove('active');
        navMenu.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  // Atualiza link ativo com base na seção visível
  function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 120;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }
}

/* ==========================================================================
   2. REQUISITO DOS FUNDADORES (INTERAÇÃO CRUCIAL)
   "ao clicar no nome Kaio Lucas A.r ou no Júlia Almeida R, mostre
    'Kaio Lucas Almeida Reis, Júlia Almeida Reis'"
   ========================================================================== */
function initFoundersInteractive() {
  const modal = document.getElementById('foundersModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const revealBox = document.getElementById('foundersRevealBox');

  // Elementos clicáveis para acionar a revelação dos fundadores
  const founderTriggers = document.querySelectorAll(
    '#btnJuliaName, #btnKaioName, .founder-trigger-inline, [data-founder]'
  );

  function openFoundersDisplay(founderName = '') {
    // 1. Abrir Modal com animação suave
    if (modal) {
      modal.classList.add('active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    // 2. Destacar o banner de revelação na página caso o modal seja fechado
    if (revealBox) {
      revealBox.style.animation = 'none';
      void revealBox.offsetWidth; // trigger reflow
      revealBox.style.animation = 'pulseBeacon 2.5s ease';
    }

    // 3. Exibir toast confirmando a exibição solicitada
    showToast(`Proprietários da ACsoft: Kaio Lucas Almeida Reis, Júlia Almeida Reis`);
  }

  function closeFoundersModal() {
    if (modal) {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  }

  founderTriggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const founder = btn.getAttribute('data-founder') || '';
      openFoundersDisplay(founder);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeFoundersModal);
  }

  // Fechar ao clicar no backdrop ou apertar ESC
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeFoundersModal();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
      closeFoundersModal();
    }
  });
}

/* ==========================================================================
   3. COPIADOR DA PALETA DE CORES
   ========================================================================== */
function initColorPaletteCopier() {
  const swatchButtons = document.querySelectorAll('.color-swatch-btn');

  swatchButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const color = btn.getAttribute('data-color');
      if (color) {
        copyToClipboard(color, `Cor ${color} copiada para a área de transferência!`);
      }
    });
  });
}

/* ==========================================================================
   4. FILTRO DE SERVIÇOS
   ========================================================================== */
function initServicesFilter() {
  const filterBtns = document.querySelectorAll('.filter-tab-btn');
  const serviceCards = document.querySelectorAll('.service-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      serviceCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
          card.style.opacity = '0';
          card.style.transform = 'translateY(15px)';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   5. CALCULADORA & SIMULADOR DE PROJETOS COM DISPATCH PARA WHATSAPP
   ========================================================================== */
function initProjectCalculator() {
  const form = document.getElementById('projectCalculatorForm');
  if (!form) return;

  const resProjectName = document.getElementById('resProjectName');
  const resTimelineEst = document.getElementById('resTimelineEst');
  const btnSendWhatsapp = document.getElementById('btnSendQuoteWhatsapp');

  const projectTypeLabels = {
    app: 'Aplicativo Mobile (iOS & Android)',
    site: 'Site Completo (Construção, Hospedagem & Segurança)',
    ferramenta: 'Ferramenta Personalizada / Automação',
    jogo: 'Jogo (Games Studio 2D/3D)'
  };

  const featureLabels = {
    design: 'Design Exclusivo & UI/UX',
    auth: 'Autenticação & Login de Usuários',
    banco: 'Banco de Dados & API na Nuvem',
    pagamento: 'Gateway de Pagamentos / Pix',
    hospedagem: 'Hospedagem & Blindagem de Segurança',
    painel: 'Painel Administrativo Web (Admin)'
  };

  const urgencyLabels = {
    normal: 'Padrão (4 a 8 semanas)',
    agil: 'Ágil / Acelerado (2 a 4 semanas)',
    expresso: 'Lançamento Prioritário (Imediato)'
  };

  function updateEstimate() {
    const selectedType = form.querySelector('input[name="projectType"]:checked')?.value || 'app';
    const checkedFeatures = Array.from(form.querySelectorAll('input[name="feature"]:checked')).map(cb => cb.value);
    const selectedUrgency = form.querySelector('input[name="urgency"]:checked')?.value || 'normal';

    const typeTitle = projectTypeLabels[selectedType] || 'Projeto Personalizado';
    const numFeatures = checkedFeatures.length;

    // Calcular estimativa de prazo
    let minWeeks = 3;
    let maxWeeks = 6;

    if (selectedType === 'app') { minWeeks += 2; maxWeeks += 3; }
    if (selectedType === 'jogo') { minWeeks += 3; maxWeeks += 5; }
    if (selectedType === 'site') { minWeeks += 1; maxWeeks += 2; }
    if (numFeatures > 4) { minWeeks += 1; maxWeeks += 2; }

    if (selectedUrgency === 'agil') {
      minWeeks = Math.max(2, minWeeks - 1);
      maxWeeks = Math.max(3, maxWeeks - 2);
    } else if (selectedUrgency === 'expresso') {
      minWeeks = Math.max(1, minWeeks - 2);
      maxWeeks = Math.max(2, maxWeeks - 3);
    }

    if (resProjectName) {
      resProjectName.textContent = `${typeTitle} (${numFeatures} recursos)`;
    }

    if (resTimelineEst) {
      resTimelineEst.innerHTML = `Prazo estimado: <strong>${minWeeks} a ${maxWeeks} semanas</strong> (${urgencyLabels[selectedUrgency]})`;
    }
  }

  // Ouvintes de alteração em tempo real
  form.addEventListener('change', updateEstimate);
  updateEstimate();

  // Enviar orçamento direto para o WhatsApp
  if (btnSendWhatsapp) {
    btnSendWhatsapp.addEventListener('click', () => {
      const selectedType = form.querySelector('input[name="projectType"]:checked')?.value || 'app';
      const checkedFeatures = Array.from(form.querySelectorAll('input[name="feature"]:checked')).map(cb => featureLabels[cb.value] || cb.value);
      const selectedUrgency = form.querySelector('input[name="urgency"]:checked')?.value || 'normal';

      const typeTitle = projectTypeLabels[selectedType] || 'Projeto';
      const featuresText = checkedFeatures.length > 0 ? checkedFeatures.join(', ') : 'Escopo básico';
      const urgencyText = urgencyLabels[selectedUrgency];

      const rawMsg = `Olá, ACsoft Studios!

Gostaria de solicitar uma proposta com base na simulação do site:
• Tipo de Projeto: ${typeTitle}
• Recursos Selecionados: ${featuresText}
• Ritmo de Lançamento: ${urgencyText}

Gostaria de agendar uma conversa com os fundadores (Kaio Lucas e Júlia Almeida) para detalhar minha ideia. Obrigado!`;

      const encodedMsg = encodeURIComponent(rawMsg);
      const whatsappUrl = `https://wa.me/5574991969827?text=${encodedMsg}`;

      window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
      showToast('Redirecionando para o WhatsApp oficial da ACsoft...');
    });
  }
}

/* ==========================================================================
   6. FAQ ACCORDION
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question-btn');
    const answerPanel = item.querySelector('.faq-answer-panel');

    if (questionBtn && answerPanel) {
      questionBtn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        // Fechar outros itens abertos
        faqItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherBtn = otherItem.querySelector('.faq-question-btn');
            const otherPanel = otherItem.querySelector('.faq-answer-panel');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
            if (otherPanel) otherPanel.style.maxHeight = null;
          }
        });

        // Alternar item atual
        if (!isActive) {
          item.classList.add('active');
          questionBtn.setAttribute('aria-expanded', 'true');
          answerPanel.style.maxHeight = answerPanel.scrollHeight + 'px';
        } else {
          item.classList.remove('active');
          questionBtn.setAttribute('aria-expanded', 'false');
          answerPanel.style.maxHeight = null;
        }
      });
    }
  });
}

/* ==========================================================================
   7. FORMULÁRIO DE CONTATO DIRETO & BOTÃO COPIAR E-MAIL
   ========================================================================== */
function initContactForm() {
  const form = document.getElementById('directContactForm');
  const feedback = document.getElementById('formFeedback');
  const copyEmailBtn = document.getElementById('btnCopyEmail');

  // Copiar E-mail oficial
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', (e) => {
      e.preventDefault();
      copyToClipboard('eukaioluccas31@gmail.com', 'E-mail eukaioluccas31@gmail.com copiado!');
    });
  }

  // Envio do formulário com integração ao WhatsApp
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('clientName')?.value.trim() || '';
      const phone = document.getElementById('clientPhone')?.value.trim() || '';
      const email = document.getElementById('clientEmail')?.value.trim() || '';
      const interest = document.getElementById('projectInterest')?.value || '';
      const message = document.getElementById('clientMessage')?.value.trim() || '';

      if (!name || !phone || !email || !interest || !message) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
      }

      const formattedMsg = `Olá, ACsoft Studios! Mensagem de Contato pelo Site:

• Nome: ${name}
• Telefone/WhatsApp: ${phone}
• E-mail: ${email}
• Interesse: ${interest}
• Mensagem: ${message}

Aguardo o retorno dos fundadores (Júlia A.R e Kaio Lucas A.R)!`;

      const encoded = encodeURIComponent(formattedMsg);
      const whatsappUrl = `https://wa.me/5574991969827?text=${encoded}`;

      if (feedback) {
        feedback.innerHTML = `✓ Mensagem recebida! Redirecionando para o WhatsApp oficial (+55 74 991969827)...`;
        feedback.className = 'form-feedback success';
      }

      setTimeout(() => {
        window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
      }, 700);
    });
  }
}

/* ==========================================================================
   8. UTILITÁRIOS: CLIPBOARD & TOAST NOTIFICATION
   ========================================================================== */
function copyToClipboard(text, successMsg = 'Copiado para a área de transferência!') {
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(successMsg);
    }).catch(() => {
      fallbackCopy(text, successMsg);
    });
  } else {
    fallbackCopy(text, successMsg);
  }
}

function fallbackCopy(text, successMsg) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.style.position = 'fixed';
  textArea.style.left = '-999999px';
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();
  try {
    document.execCommand('copy');
    showToast(successMsg);
  } catch (err) {
    console.error('Falha ao copiar:', err);
  }
  document.body.removeChild(textArea);
}

let toastTimeout;
function showToast(message) {
  const toast = document.getElementById('siteToast');
  const toastMessage = document.getElementById('toastMessage');

  if (!toast || !toastMessage) return;

  toastMessage.textContent = message;
  toast.classList.add('active');

  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.remove('active');
  }, 4000);
}

/* ==========================================================================
   9. ANIMAÇÕES DE SCROLL (INTERSECTION OBSERVER)
   ========================================================================== */
function initScrollAnimations() {
  if (!('IntersectionObserver' in window)) return;

  const cardsToAnimate = document.querySelectorAll(
    '.service-card, .pillar-card, .founder-card, .visual-card, .gallery-item-card, .equation-box'
  );

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  cardsToAnimate.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(24px)';
    card.style.transition = 'opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)';
    observer.observe(card);
  });
}
