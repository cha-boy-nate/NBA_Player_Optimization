# NBA_Player_Optimization
<ol>
<li>
<h2>Introduction</h2>
</li>
<p>In 2002 general manager of the Oakland Athletics, Billy Beane, proved it feasible to compose a successful data driven professional sports team. Billy intentionally avoided watching his team’s games to eliminate the formation of player preference; thus keeping each decision as objective and unbiased as possible. Each player chosen to the team was statistically evaluated and selected in order to optimize the highest skill for the lowest price. Notably, while maintaining the third lowest salary tax in the MLB, the Oakland Athletics won the American League Championship that year. After three divisional titles Billy Beane demonstrated the power of data by proving his effectiveness in optimizing skill for salary. Despite having a fraction of the budget, the A’s performed significantly better than their competition. (Ford, 2016).</p>
<p>The goal for sports teams is always hiring the best players they can, with the money that they have available. A problem sports general managers like Billy Beane face, is determining how successful their selection has been compared to the most optimum selection. By comparing their choice of players to the optimum selection of players; general managers can improve quality of selection in the future. The best possible selection is calculated by applying an optimum combination algorithm for a set of elements that minimizes the weight and maximizes the value. </p>
<p>Skill will be measured by taking the Player Efficiency Rating (PER) over the past season. Cost will be measured in U.S. dollars according to the active player contracts. Skill and cost data are updated and published according to the league’s generated statistics; by game and by season respectfully. Only the free agents that are registered by the league will be considered.</p>

<li>
<h2>Background</h2>
</li>

<p>This problem aims to apply Beane’s ideas to NBA Teams. ESPN analyst John Hollinger published his book Pro Basketball Prospectus revolutionizing the world of professional basketball in the United States. Hollinger’s Player Efficiency Rating (PER), explained in his book, compiled every aspect of the game into a single number to represent a player’s strengths and weaknesses (Hollinger, 2003). Since the book was published, PER has been a key component during the selection of a player for employment. Thus, John Hollinger’s Player Efficiency Rating will be used as the value for this combinatorial optimization problem.</p>

<p>The goal of this project was to apply a heuristic solution to a real-world Nondeterministic Polynomial (NP) Problem. NP problems are decision problems in which there may or may not exist a solution with polynomial runtime. This scenario is modeled after the Knapsack Problem; a NP-Hard optimization problem. The goal is to calculate which items to include in a knapsack without exceeding it’s set weight limit; optimizing selection for the highest value.</p>

<p>In this case, each player’s weight is their cost; skill is associated with their value. Weight will be determined by the yearly cost of each player’s contract. Contracts are calculated by dividing the total worth of the contract, bonuses included, by the number of years in contract. This number represents an estimation of how much the current team is paying the specific player for 2019. Value will be determined by using Hollinger’s Player Efficiency Rating [see appendix B]. The distribution of player’s weight to player’s value shows a positive increasing relationship. But an increase in a player’s salary does not guarantee in an equal growth of weight, highlighted some of the difficulties general managers have when selecting players.</p>

<li>
<h2>Solution Description</h2>
</li>

<p>Data has been collected from various locations produced by the same source. The basketball reference records player name, PER, and Salary according to the NBA’s published records. PER is calculated per game and factored into player’s season average at the end of every game. No games after March 7, 2019 will be included in the dataset. Only player that have been listed in free agency during the year 2019 will be considered (75 players total). Salary is calculated at the start of the season when teams are required to report their players contract deals to the National Basketball Player’s Association. Each player has a weight (salary) and a value (player efficiency rating).</p>

<li>
<h2>Results</h2>
</li>

<p>Since the solution was implemented recursively; the achieved time complexity was O(2ⁿ). The optimal way to implement this would be iteratively. When recursion is used comparisons end up being repeated. This is called the overlapping subproblem property (Mital, 2018). If the implementation was done iteratively using dynamic programming the overlapping subproblem would be avoided and the time complexity would have been O(nW). Since the dataset was only about seventy rows long execution only consumed about 15.02 seconds. With O(2ⁿ) as the time complexity, had the dataset been larger the execution time would have taken much longer.</p>
<p>This graph shows the performance of an iterative versus a recursive power function. Once the values start to get bigger the iterative function does much better performance wise. However, with values under two hundred fifty the values for recursive performance is very similar to that of the iterative performance. With seventy rows of data, implementing it iteratively or recursively would have a negligible difference in performance.</p>

<li>
<h2>Conclusions</h2>
</li>

<p>Running the implementation of this combination optimization problem provides practice applying nondeterministic polynomial algorithms to real world data. Real world data can be considerably larger than test data; forcing developers to take into account every line of code that is used. Additionally, the algorithm’s time complexity greatly depends on the data available. Developers should consider the available data, when determining if a solution can be created in an efficient amount of time. Heuristics and optimum combination problems are especially valuable in data science but can be applied to nearly every industry from medicine to sports. The amount of available data is growing exponentially, increasing applicability and importance of speed. Heuristics can be especially useful in scenarios that require very quick decisions that, without heuristic algorithms, could not be solved in any reasonable amount of time. </p>
<p>Knapsack optimization problems are especially useful when dealing with a relatively low weight limit, but a high goal in mind for total value as in the case of Billy Beane’s budget problem. Implementing a solution to this problem has helped create a better understanding of how to write good code and solve problems in efficient ways.</p>

<li>
<h2>References</h2>
</li>

<ol>

<li>
  Hollinger, J. (2003). Pro Basketball Prospectus. Brassey's, Inc.
</li>

<li>
  National Basketball Players Association. (2017, 7 1). nbpa.com/cba/. Retrieved from http://3c90sm37lsaecdwtr32v9qof-wpengine.netdna-ssl.com/wp-content/uploads/2016/02/2017-NBA-NBPA-Collective-Bargaining-Agreement.pdf
</li>

<li>
  Ford, E. (2016, August 31). Moneyball: How Big Data & Analytics Turned The Oakland A's Into The Best Team In Baseball. Retrieved March 15, 2019, from https://thesportsmarketingplaybook.com/2016/08/31/moneyball-how-big-data-analytics-turned-the-oakland-as-into-the-best-team-in-baseball/ 
<li>

<li>
  Mital, N. (2018, September 05). Overlapping Subproblems Property in Dynamic Programming | DP-1. Retrieved March 15, 2019, from https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
</li>

<li>
  Kleinberg, J., & Tardos, E. (2014). Algorithm design. Noida: Pearson india Education Services Pvt. 8 | Page NP Problem
</li>

<li>
2018-19 NBA Player Stats: Advanced. (n.d.). Retrieved from https://www.basketball-reference.com/leagues/NBA_2019_advanced.html
</li>

<li>
2018-19 NBA Player Contracts. (n.d.). Retrieved from https://www.basketball-reference.com/contracts/players.html</p>
</li>
</ol>

</ol>
