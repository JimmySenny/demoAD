#include "comm.h"

void printNums( int * nums, int numsSize ){
    printf( "[" );

    for( int i = 0; i < numsSize; i++ ){
        printf("%d ", nums[i] );
    }

    printf( "]\n" );
    return;
}

void printString( char * str, int strSize ){
    printf( "[" );

    for( int i = 0; i < strSize; i++ ){
        printf("%c ", str[i] );
    }

    printf( "]\n" );


    return;
}
