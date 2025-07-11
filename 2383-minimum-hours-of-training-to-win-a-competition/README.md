<h2><a href="https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/">2383. Minimum Hours of Training to Win a Competition</a></h2><h3>Easy</h3><hr><div bis_skin_checked="1"><p>You are entering a competition, and are given two <strong>positive</strong> integers <code>initialEnergy</code> and <code>initialExperience</code> denoting your initial energy and initial experience respectively.</p>

<p>You are also given two <strong>0-indexed</strong> integer arrays <code>energy</code> and <code>experience</code>, both of length <code>n</code>.</p>

<p>You will face <code>n</code> opponents <strong>in order</strong>. The energy and experience of the <code>i<sup>th</sup></code> opponent is denoted by <code>energy[i]</code> and <code>experience[i]</code> respectively. When you face an opponent, you need to have both <strong>strictly</strong> greater experience and energy to defeat them and move to the next opponent if available.</p>

<p>Defeating the <code>i<sup>th</sup></code> opponent <strong>increases</strong> your experience by <code>experience[i]</code>, but <strong>decreases</strong> your energy by <code>energy[i]</code>.</p>

<p>Before starting the competition, you can train for some number of hours. After each hour of training, you can <strong>either</strong> choose to increase your initial experience by one, or increase your initial energy by one.</p>

<p>Return <em>the <strong>minimum</strong> number of training hours required to defeat all </em><code>n</code><em> opponents</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> You can increase your energy to 11 after 6 hours of training, and your experience to 5 after 2 hours of training.
You face the opponents in the following order:
- You have more energy and experience than the 0<sup>th</sup> opponent so you win.
  Your energy becomes 11 - 1 = 10, and your experience becomes 5 + 2 = 7.
- You have more energy and experience than the 1<sup>st</sup> opponent so you win.
  Your energy becomes 10 - 4 = 6, and your experience becomes 7 + 6 = 13.
- You have more energy and experience than the 2<sup>nd</sup> opponent so you win.
  Your energy becomes 6 - 3 = 3, and your experience becomes 13 + 3 = 16.
- You have more energy and experience than the 3<sup>rd</sup> opponent so you win.
  Your energy becomes 3 - 2 = 1, and your experience becomes 16 + 1 = 17.
You did a total of 6 + 2 = 8 hours of training before the competition, so we return 8.
It can be proven that no smaller answer exists.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You do not need any additional energy or experience to win the competition, so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == energy.length == experience.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= initialEnergy, initialExperience, energy[i], experience[i] &lt;= 100</code></li>
</ul>
</div>