#include <stdio.h>
#include <stdlib.h>

int main()
{
    double dRaio = 0;
    double dPi = 3.14159;
    double dArea = 0;

    scanf("%lf",&dRaio);
    dArea = dPi*(dRaio*dRaio);

    printf("A=%.4lf\n",dArea);



    return 0;
}