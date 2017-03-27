
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

import edu.princeton.cs.algs4.QuickFindUF;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

   private int gridSize;
   private boolean[][] openGrid;
   private WeightedQuickUnionUF gridUnion;
   // private QuickFindUF gridUnion;

   private int openSites;

   public Percolation(int n)                // create n-by-n grid, with all sites blocked
   {
      gridSize = n;
      openGrid = new boolean[gridSize][gridSize];
      gridUnion = new WeightedQuickUnionUF(gridSize * gridSize);
      //gridUnion = new QuickFindUF(gridSize * gridSize);

      openSites = 0;
   }

   public void open(int row, int col)    // open site (row, col) if it is not open already
   {
      if (row < 0 || row >= gridSize) return;
      if (col < 0 || col >= gridSize) return;

      if (openGrid[row][col])
         return;

      // StdOut.println("Open position (" + row + "," + col + ")");

      openSites = openSites + 1;
      openGrid[row][col] = true;

      connectTo(row, col, row - 1, col);
      connectTo(row, col, row + 1, col);

      connectTo(row, col, row, col + 1);
      connectTo(row, col, row, col - 1);

   }

   private void connectTo(int newRow, int newCol, int row, int col)
   {
      if (row < 0 || row >= gridSize) return;
      if (col < 0 || col >= gridSize) return;

      if (!openGrid[row][col]) return;

      // StdOut.println("Union position (" + row + "," + col + ") to (" + newRow + "," + newCol + ")");
      gridUnion.union(newRow*gridSize + newCol, row*gridSize + col);
   }

   public boolean isOpen(int row, int col)  // is site (row, col) open?
   {
      if (row < 0 || row >= gridSize) return false;
      if (col < 0 || col >= gridSize) return false;

      return openGrid[row][col];
   }

   public boolean isFull(int row, int col)  // is site (row, col) full?
   {
      if (row < 0 || row >= gridSize) return false;
      if (col < 0 || col >= gridSize) return false;
      if (!openGrid[row][col]) return false;


      for (int i = 0; i < gridSize; i++)
      {
         if (openGrid[0][i] &&
               gridUnion.connected(row*gridSize + col, i)) 
            return true;
      }

      return false;
   }

   public int numberOfOpenSites()       // number of open sites
   {
      return openSites;
   }

   public boolean percolates()              // does the system percolate?
   {
      for (int j = 0; j < gridSize; j++)
      {
         if (isFull(gridSize-1, j))
            return true;
      }

      return false;
   }

   // private void printGrid()
   // {
   //    String line = "";
   //    for (int i = 0; i < gridSize; i++)
   //    {
   //       line = "";

   //       for (int j = 0; j < gridSize; j++)
   //       {
   //          if (openGrid[i][j])
   //             line += " " + 1;
   //          else
   //             line += " " + 0;
   //       }
   //       StdOut.println(line);
   //    }
   // }

   public static void main(String[] args)   // test client (optional)
   {
      String sizeString = args[0];
      int size = Integer.parseInt(sizeString);

      // StdOut.println("Testing Percolation with size " + sizeString);
      Percolation p = new Percolation(size);

      int maxOpen =  size * size * size; //StdRandom.uniform(size*size);

      int i = 0;
      boolean alreadyPercolated = false;

      while (i < maxOpen && !alreadyPercolated)
      {
         p.open(StdRandom.uniform(size), StdRandom.uniform(size));
         alreadyPercolated = p.percolates();
         i++;
      }

      // if (alreadyPercolated)
      //    StdOut.println("Percolated with interation " + i);
      // else 
      //    StdOut.println("It does not percolated ");

      // p.printGrid();

   }
}