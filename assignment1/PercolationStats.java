import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;

public class PercolationStats {
  private double[] samples;
  private double samplesTrials;

  public PercolationStats(int n, int trials)    // perform trials independent experiments on an n-by-n grid
  {
    samplesTrials = trials;

    Percolation p = null;
    boolean alreadyPercolated = false;

    int gridSize = n * n;

    samples = new double[trials];

    for (int i = 0; i < trials; i++)
    {
      p = new Percolation(n);

      alreadyPercolated = false;

      while (!alreadyPercolated)
      {
         p.open(StdRandom.uniform(n), StdRandom.uniform(n));
         alreadyPercolated = p.percolates();
      }

      samples[i] = ((double)p.numberOfOpenSites()) / gridSize;
      //StdOut.println("Testing Percolation with size samples[" + i + "] = " + samples[i] + " due to number of open sites " + 
      // p.numberOfOpenSites());


    }
  }

  public double mean()                          // sample mean of percolation threshold
  {
    return StdStats.mean(samples);
  }

  public double stddev()                        // sample standard deviation of percolation threshold
  {
    return StdStats.stddev(samples);
  }

  public double confidenceLo()                  // low  endpoint of 95% confidence interval
  {
  return mean() - (1.96 * stddev()) / Math.sqrt(samplesTrials);
  }

  public double confidenceHi()                  // high endpoint of 95% confidence interval
  {
  return mean() + (1.96 * stddev()) / Math.sqrt(samplesTrials);
  }

  public static void main(String[] args)        // test client (described below)
  {
    Stopwatch stopwatch = new Stopwatch();

    String sizeString = args[0];
    int size = Integer.parseInt(sizeString);

    String tString = args[1];
    int t = Integer.parseInt(tString);

    // StdOut.println("Testing Percolation with size " + sizeString + " and " + tString + " samples");

    PercolationStats ps = new PercolationStats(size, t);
    StdOut.println("mean\t\t\t= " + ps.mean() );
    StdOut.println("stddev\t\t\t= " + ps.stddev() );
    StdOut.println("95% confidence interval = [" + ps.confidenceLo() + ", " + ps.confidenceHi() + "]" );

    StdOut.println("\nTotal time " + stopwatch.elapsedTime());

    
  }
}