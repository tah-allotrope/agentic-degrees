/*
 * Shared quiz engine. Dependency-free vanilla JavaScript.
 * Finds every <section class="quiz">, renders each <li data-answer="..."> option
 * inside a .options list as a clickable button, reveals correct/incorrect
 * immediately on click, and shows a running score per quiz.
 *
 * Expected markup:
 *   <section class="quiz">
 *     <ol>
 *       <li class="q">
 *         <p class="qtext">Question?</p>
 *         <ul class="options">
 *           <li data-answer="true">Right option</li>
 *           <li data-answer="false">Wrong option</li>
 *         </ul>
 *       </li>
 *     </ol>
 *   </section>
 */
(function () {
  "use strict";

  function initQuiz(section) {
    var questions = section.querySelectorAll(".q");
    if (questions.length === 0) {
      return;
    }

    var scoreBox = document.createElement("div");
    scoreBox.className = "quiz-score";
    scoreBox.textContent = "Score: 0 / " + questions.length;
    section.appendChild(scoreBox);

    var correct = 0;

    questions.forEach(function (question) {
      var options = question.querySelectorAll(".options li[data-answer]");
      var answered = false;

      options.forEach(function (option) {
        option.addEventListener("click", function () {
          if (answered) {
            return;
          }
          answered = true;
          var isCorrect = option.getAttribute("data-answer") === "true";
          if (isCorrect) {
            option.classList.add("correct");
            correct += 1;
          } else {
            option.classList.add("wrong");
          }
          options.forEach(function (other) {
            other.classList.add("disabled");
            if (other !== option && other.getAttribute("data-answer") === "true") {
              other.classList.add("correct");
            }
          });
          scoreBox.textContent = "Score: " + correct + " / " + questions.length;
        });
      });
    });
  }

  document.querySelectorAll("section.quiz").forEach(initQuiz);
})();
