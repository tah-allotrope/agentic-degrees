/* teach-workspace quiz widget — instant feedback, per-quiz score, reset.
   Markup contract:
     <div class="quiz" id="...">
       <div class="q" data-answer="2">            <!-- index of correct option, 0-based -->
         <div class="prompt">Question text</div>
         <div class="options">
           <button class="opt">option A</button>
           <button class="opt">option B</button>
           ...
         </div>
         <div class="explain">Why this is the answer</div>
       </div>
       ...
       <div class="quiz-score"></div>
       <button class="quiz-reset">Reset quiz</button>
     </div>
   Author rule: every option in one question must have the SAME word count. */
(function () {
  function initQuiz(quiz) {
    var questions = quiz.querySelectorAll('.q[data-answer]');
    var scoreEl = quiz.querySelector('.quiz-score');
    var answered = 0, correct = 0;

    function updateScore() {
      if (!scoreEl) return;
      var remaining = questions.length - answered;
      scoreEl.textContent = 'Answered ' + answered + ' of ' + questions.length +
        ' — ' + correct + ' correct' + (remaining ? ' (' + remaining + ' left)' : '');
      if (answered === questions.length) {
        scoreEl.textContent += ' — final score ' + correct + '/' + questions.length +
          (correct === questions.length ? '. Perfect retrieval — well done.' : '. Review the misses and retake.');
      }
    }

    questions.forEach(function (q) {
      var correctIndex = parseInt(q.getAttribute('data-answer'), 10);
      var opts = q.querySelectorAll('.opt');
      opts.forEach(function (btn, i) {
        btn.addEventListener('click', function () {
          if (q.classList.contains('answered')) return;
          q.classList.add('answered');
          answered += 1;
          opts.forEach(function (o) { o.disabled = true; });
          if (i === correctIndex) {
            btn.classList.add('correct');
            correct += 1;
          } else {
            btn.classList.add('wrong');
            opts[correctIndex].classList.add('correct');
          }
          updateScore();
        });
      });
    });

    var reset = quiz.querySelector('.quiz-reset');
    if (reset) {
      reset.addEventListener('click', function () {
        questions.forEach(function (q) {
          q.classList.remove('answered');
          q.querySelectorAll('.opt').forEach(function (o) {
            o.disabled = false;
            o.classList.remove('correct', 'wrong');
          });
        });
        answered = 0; correct = 0;
        updateScore();
      });
    }
    updateScore();
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.quiz').forEach(initQuiz);
  });
})();
