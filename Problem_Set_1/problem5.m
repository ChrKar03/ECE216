x = [50 250 500 1000];

ff_u = [47 245 494 994];
bf_u = [29 140 280 559];

ff_l = [43 241 490 990];
bf_l = [16 75 149 297];

plot(x, ff_u, x, bf_u, x, ff_l, x, bf_l)
legend('First-Fit Uni-Dist', 'Best-Fit Uni-Dist', 'First-Fit Log-Dist', 'Best-Fit Log-Dist')