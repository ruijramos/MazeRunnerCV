import java.util.*;
import java.io.*;

public class mazeRunner {

	public static void clearConsole(){
	    // Clears Screen 
	    try {
	        if (System.getProperty("os.name").contains("Windows"))
	            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
	        else
	            Runtime.getRuntime().exec("clear");
	    } catch (IOException | InterruptedException ex) {}
	}

	public static String[][] buildMaze(int mazeNumber) {
		String gameField[][] = new String[20][20];

		// Playing field
		for(int i=0; i<20; i++) {
			for(int j=0; j<20; j++) {
				gameField[i][j] = " ";
			}
		}

		// Borders
		for(int j=0; j<20; j++) {
			gameField[0][j] = "\u25A0";
			gameField[19][j] = "\u25A0";
		}
		for(int i=0; i<20; i++) {
			if(i!=1) gameField[i][0] = "\u25A0";
			if(i!=18) gameField[i][19] = "\u25A0";
		}

		// Walls
		switch(mazeNumber) {
			case 1:
				gameField[1][16] = "\u25A0";
				gameField[1][17] = "\u25A0";
				gameField[1][18] = "\u25A0";
				gameField[2][0] = "\u25A0";
				gameField[2][1] = "\u25A0";
				gameField[2][3] = "\u25A0";
				gameField[2][4] = "\u25A0";
				gameField[2][5] = "\u25A0";
				gameField[2][7] = "\u25A0";
				gameField[2][8] = "\u25A0";
				gameField[2][9] = "\u25A0";
				gameField[2][10] = "\u25A0";
				gameField[2][11] = "\u25A0";
				gameField[2][12] = "\u25A0";
				gameField[2][14] = "\u25A0";
				gameField[3][1] = "\u25A0";
				gameField[3][3] = "\u25A0";
				gameField[3][4] = "\u25A0";
				gameField[3][5] = "\u25A0";
				gameField[3][11] = "\u25A0";
				gameField[3][12] = "\u25A0";
				gameField[3][13] = "\u25A0";
				gameField[3][14] = "\u25A0";
				gameField[3][15] = "\u25A0";
				gameField[3][16] = "\u25A0";
				gameField[3][17] = "\u25A0";
				gameField[4][3] = "\u25A0";
				gameField[4][4] = "\u25A0";
				gameField[4][8] = "\u25A0";
				gameField[4][9] = "\u25A0";
				gameField[4][13] = "\u25A0";
				gameField[4][14] = "\u25A0";
				gameField[4][16] = "\u25A0";
				gameField[4][17] = "\u25A0";
				gameField[5][1] = "\u25A0";
				gameField[5][2] = "\u25A0";
				gameField[5][3] = "\u25A0";
				gameField[5][4] = "\u25A0";
				gameField[5][5] = "\u25A0";
				gameField[5][6] = "\u25A0";
				gameField[5][7] = "\u25A0";
				gameField[5][8] = "\u25A0";
				gameField[5][9] = "\u25A0";
				gameField[5][10] = "\u25A0";
				gameField[5][11] = "\u25A0";
				gameField[5][13] = "\u25A0";
				gameField[5][14] = "\u25A0";
				gameField[5][17] = "\u25A0";
				gameField[6][1] = "\u25A0";
				gameField[6][2] = "\u25A0";
				gameField[6][13] = "\u25A0";
				gameField[6][14] = "\u25A0";
				gameField[6][15] = "\u25A0";
				gameField[6][16] = "\u25A0";
				gameField[6][17] = "\u25A0";
				gameField[6][18] = "\u25A0";
				gameField[7][1] = "\u25A0";
				gameField[7][2] = "\u25A0";
				gameField[7][4] = "\u25A0";
				gameField[7][6] = "\u25A0";
				gameField[7][7] = "\u25A0";
				gameField[7][8] = "\u25A0";
				gameField[7][9] = "\u25A0";
				gameField[7][10] = "\u25A0";
				gameField[7][11] = "\u25A0";
				gameField[7][14] = "\u25A0";
				gameField[7][15] = "\u25A0";
				gameField[7][16] = "\u25A0";
				gameField[7][17] = "\u25A0";
				gameField[7][18] = "\u25A0";
				gameField[8][4] = "\u25A0";
				gameField[8][10] = "\u25A0";
				gameField[8][11] = "\u25A0";
				gameField[8][12] = "\u25A0";
				gameField[9][2] = "\u25A0";
				gameField[9][4] = "\u25A0";
				gameField[9][6] = "\u25A0";
				gameField[9][7] = "\u25A0";
				gameField[9][8] = "\u25A0";
				gameField[9][10] = "\u25A0";
				gameField[9][11] = "\u25A0";
				gameField[9][12] = "\u25A0";
				gameField[9][13] = "\u25A0";
				gameField[9][14] = "\u25A0";
				gameField[9][15] = "\u25A0";
				gameField[9][16] = "\u25A0";
				gameField[9][17] = "\u25A0";
				gameField[10][2] = "\u25A0";
				gameField[10][4] = "\u25A0";
				gameField[10][6] = "\u25A0";
				gameField[10][7] = "\u25A0";
				gameField[10][8] = "\u25A0";
				gameField[10][11] = "\u25A0";
				gameField[10][17] = "\u25A0";
				gameField[11][2] = "\u25A0";
				gameField[11][4] = "\u25A0";
				gameField[11][6] = "\u25A0";
				gameField[11][7] = "\u25A0";
				gameField[11][8] = "\u25A0";
				gameField[11][9] = "\u25A0";
				gameField[11][10] = "\u25A0";
				gameField[11][11] = "\u25A0";
				gameField[11][13] = "\u25A0";
				gameField[11][15] = "\u25A0";
				gameField[11][17] = "\u25A0";
				gameField[12][1] = "\u25A0";
				gameField[12][2] = "\u25A0";
				gameField[12][4] = "\u25A0";
				gameField[12][7] = "\u25A0";
				gameField[12][11] = "\u25A0";
				gameField[12][13] = "\u25A0";
				gameField[12][15] = "\u25A0";
				gameField[12][17] = "\u25A0";
				gameField[13][1] = "\u25A0";
				gameField[13][2] = "\u25A0";
				gameField[13][4] = "\u25A0";
				gameField[13][5] = "\u25A0";
				gameField[13][6] = "\u25A0";
				gameField[13][7] = "\u25A0";
				gameField[13][9] = "\u25A0";
				gameField[13][10] = "\u25A0";
				gameField[13][11] = "\u25A0";
				gameField[13][13] = "\u25A0";
				gameField[13][15] = "\u25A0";
				gameField[13][17] = "\u25A0";
				gameField[14][1] = "\u25A0";
				gameField[14][4] = "\u25A0";
				gameField[14][5] = "\u25A0";
				gameField[14][6] = "\u25A0";
				gameField[14][11] = "\u25A0";
				gameField[14][13] = "\u25A0";
				gameField[14][15] = "\u25A0";
				gameField[14][17] = "\u25A0";
				gameField[15][1] = "\u25A0";
				gameField[15][3] = "\u25A0";
				gameField[15][4] = "\u25A0";
				gameField[15][5] = "\u25A0";
				gameField[15][6] = "\u25A0";
				gameField[15][8] = "\u25A0";
				gameField[15][9] = "\u25A0";
				gameField[15][11] = "\u25A0";
				gameField[15][13] = "\u25A0";
				gameField[15][15] = "\u25A0";
				gameField[15][17] = "\u25A0";
				gameField[16][1] = "\u25A0";
				gameField[16][3] = "\u25A0";
				gameField[16][4] = "\u25A0";
				gameField[16][5] = "\u25A0";
				gameField[16][6] = "\u25A0";
				gameField[16][8] = "\u25A0";
				gameField[16][9] = "\u25A0";
				gameField[16][11] = "\u25A0";
				gameField[16][13] = "\u25A0";
				gameField[16][15] = "\u25A0";
				gameField[16][17] = "\u25A0";
				gameField[16][18] = "\u25A0";
				gameField[17][1] = "\u25A0";
				gameField[17][8] = "\u25A0";
				gameField[17][9] = "\u25A0";
				gameField[17][13] = "\u25A0";
				gameField[17][15] = "\u25A0";
				gameField[17][17] = "\u25A0";
				gameField[17][18] = "\u25A0";
				gameField[18][1] = "\u25A0";
				gameField[18][3] = "\u25A0";
				gameField[18][4] = "\u25A0";
				gameField[18][5] = "\u25A0";
				gameField[18][6] = "\u25A0";
				gameField[18][10] = "\u25A0";
				gameField[18][11] = "\u25A0";
				gameField[18][12] = "\u25A0";
				gameField[18][13] = "\u25A0";
				gameField[18][14] = "\u25A0";
				gameField[18][15] = "\u25A0";
				break;
			case 2:

				break;
			case 3:

				break;
			default:
				break;
		}

		return gameField;
	}

	public static void printGameField(String[][] gameField, int posX, int posY) {
        System.out.println("---------------------------------------");
        System.out.println("|            Maze Runner!             |");
        System.out.println("---------------------------------------");
 
		for(int i=0; i<20; i++) {
			System.out.println();
			for(int j=0; j<20; j++) {
				if(i==posX && j==posY) {
					System.out.print("\u231B" + " ");
					continue;
				}
				System.out.print(gameField[i][j] + " ");
			}
		}

		System.out.println();
	}

	public static boolean possiblePlay(String[][] gameField, int posX, int posY, String direction) {
		switch(direction) {
			case "A":
				if(posX == 1 && posY == 0) return false;
				if(gameField[posX][posY-1].equals(" ")) return true;
				return false;
        	case "S":
        		if(gameField[posX+1][posY].equals(" ")) return true;
				return false;
        	case "D":
        		if(gameField[posX][posY+1].equals(" ")) return true;
				return false;
        	case "W":
        		if(gameField[posX-1][posY].equals(" ")) return true;
				return false;
		}
		return false;
	}

    public static void main(String[] args) {
    	Scanner read = new Scanner(System.in);
    	clearConsole();
    	
    	// Important Variables
    	String gameField[][] = new String[20][20];
    	int actualPosition_X = 1;
    	int actualPosition_Y = 0;
    	int finalPosition_X = 18;
    	int finalPosition_Y = 19;

    	// Game presentation and maze choice
        System.out.println();
        System.out.println("---------------------------");
        System.out.println("| Welcome to Maze Runner! |");
        System.out.println("---------------------------");
        System.out.println();
        System.out.print("Please, select the Maze you want to play, from 1 to 3: ");
        int choosenMaze = read.nextInt();

        // Building Maze
        gameField = buildMaze(choosenMaze);
        read.nextLine();

        // Let's start playing!
        clearConsole();
        while(actualPosition_X != finalPosition_X || actualPosition_Y != finalPosition_Y) {
        	clearConsole();
        	printGameField(gameField, actualPosition_X, actualPosition_Y);
        	
        	String chooseDirection = read.nextLine();

        	switch(chooseDirection) {
        		case "A":
        		 	if(possiblePlay(gameField, actualPosition_X, actualPosition_Y, "A")) {
        		 		actualPosition_Y = actualPosition_Y-1;
        		 	}
        			break;
        		case "S":
        			if(possiblePlay(gameField, actualPosition_X, actualPosition_Y, "S")) {
        				actualPosition_X = actualPosition_X + 1;
        		 	}
        			break;
        		case "D":
        			if(possiblePlay(gameField, actualPosition_X, actualPosition_Y, "D")) {
        				actualPosition_Y = actualPosition_Y + 1;
        		 	}
        			break;
        		case "W":
        			if(possiblePlay(gameField, actualPosition_X, actualPosition_Y, "W")) {
        				actualPosition_X = actualPosition_X - 1;
        		 	}
        			break;
        	}
        }

        clearConsole();
        printGameField(gameField, actualPosition_X, actualPosition_Y);
        System.out.println("---------------------------------------");
        System.out.println("|                WINNER                |");
        System.out.println("---------------------------------------");



    }
}