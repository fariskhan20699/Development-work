#include <iostream>
using namespace std;
int currentPlayer;
char currentMaker;

char board[3][3] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'}
};
// Draw board
void drawBoard()
{
    cout<<" " << board[0][0]<<" | "<<board[0][1]<<" | "<<board[0][2]<<"\n";
    cout<<"---|---|---\n";

    cout<<" "<<board[1][0]<<" | "<<board[1][1]<<" | "<<board[1][2]<<"\n";
    cout<<"---|---|---\n";

    cout<<" " <<board[2][0]<<" | "<<board[2][1]<<" | "<<board[2][2]<<"\n";
}

// Check whether slot is available
bool marker(int slot)
{
    int row = (slot - 1)/3;
    int column = (slot - 1)%3;

    if(board[row][column] != 'X' && board[row][column] != 'O'){
        board[row][column] = currentMaker;
        return true;
    }
    else{
        return false;
    }
}

// Check winner
int winner()
{
    // Rows
    for(int i=0;i<3;i++){
        if(board[i][0] == board[i][1] && board[i][1] == board[i][2]){
            return currentPlayer;
        }
    }

    // Columns
    for (int i=0;i<3;i++){
        if(board[0][i] == board[1][i] && board[1][i] == board[2][i]){
            return currentPlayer;
        }
    }

    // Main diagonal
    if(board[0][0] == board[1][1] && board[1][1] == board[2][2]){
        return currentPlayer;
    }

    // Other diagonal
    if(board[0][2] == board[1][1] && board[1][1] == board[2][0]){
        return currentPlayer;
    }
    return 0;
}

// Switch player and marker
void swapPlayerAndMarker(){

    if(currentMaker == 'X'){
        currentMaker = 'O';
    }
    else{
        currentMaker = 'X';
    }

    if(currentPlayer == 1){
        currentPlayer = 2;
    }
    else{
        currentPlayer = 1;
    }
}

// Game function
void game()
{
    cout<<"Choose Your Marker: X or O\n";

    char choice1;
    cin>>choice1;

    // Validate marker
    while(choice1 != 'X' && choice1 != 'O')
    {
        cout<<"Invalid marker. Please choose X or O: ";
        cin>>choice1;
    }

    currentPlayer = 1;
    currentMaker = choice1;

    drawBoard();

    int playerWin=0;

    for(int i=0;i<9;i++){
        cout<<"\nPlayer "<<currentPlayer<< " ("<<currentMaker << ")"<<", enter your turn: ";
        int slot;
        cin>>slot;

        // Check valid slot
        if (slot<1 || slot>9)
        {
            cout<<"Invalid choice. Try again!\n";
            i--;
            continue;
        }

        // Check occupied slot
        if(!marker(slot)){
            cout << "Slot is occupied. Try again!\n";
            i--;
            continue;
        }
        drawBoard();

        // Check winner
        playerWin = winner();

        if(playerWin == 1){
            cout<<"\nPlayer 1 Winner!\n";
            return;
        }

        if(playerWin == 2){
            cout<<"\nPlayer 2 Winner!\n";
            return;
        }

        // Switch player
        swapPlayerAndMarker();
    }

    // If all 9 moves completed and nobody won
    cout<<"\nTie Match!\n";
}

int main(){
    game();

    return 0;
}
