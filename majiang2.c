#include<stdio.h>
int score = 0;
int oldscore = 0;
int currentDui1 = 0;
int currentDui2 = 0;
int allDui = 0;
int flagDui = 0;

void sort(char *p,int n)
{
	int i,j;
	char temp;
	if (n < 2)  return;
	for (i = 0; i < n - 1; i++)
	{
		for (j = 0; j < n - i - 1; j++)
		{
			if(p[j]>p[j+1]) 
			{
				temp = p[j];
				p[j] = p[j+1];
				p[j+1] = temp;
			}
		}
	}
	return ;
}


int Group3Shunzi(char *p,int n)
{
	char *q,*w;
	int i,j,k,m,l,sp = 0;
	m=0;
	q = p;
	w = p;
	if ( n == 0)
	{
		return 0;
	}
	for(i = 0; i < n - 2; i++)
	{
		if (*(q+i+1) == *(q+i) && *(q+i+2)== *(q+i+1))
		{
			score += 3;
			if (i == n - 3 )										//把这三个元素移除，把后面的元素往前移动三格
			{
				*(q+i) = '\0';
				n -= 3;
				i--;
				continue;				
			}
			else
						{
							*(q + i) = '0';
							*(q + i+1) = '0';
							*(q + i+2) = '0';
							for (m = 0,l = 0;l < n ; l++)
							{
								if (*(q + l) != '0')
								{
									*(w + (m++)) = *(q + l);
								}
							}
							n = m;
							q = w;
							i--;
							continue;
						}
		}
		for (j = i+1;j < n - 1; j++ )
		{

			if (*(q + j) - *(q + i) == 1)
			{
				for (k = j + 1; k < n ; k++ )
				{
					if (*(q + k) - *(q + j) == 1)
					{
						score += 3;
						if (i == n - 3 )										//把这三个元素移除，把后面的元素往前移动三格
						{
							*(q+i) = '\0';
							n -= 3;
							i--;
							break;				
						}	
						else
						{
							*(q + i) = '0';
							*(q + j) = '0';
							*(q + k) = '0';
							for (m = 0,l = 0;l < n ; l++)
							{
								if (*(q + l) != '0')
								{
									*(w + (m++)) = *(q + l);
								}
							}
							n = m;
							q = w;
							i--;
							break;
						}	
					}
				}
			}
			continue;
		}
	}
	
}


void calDui(char *pb,int b,char *pt,int t,char *pw,int w)
{
	int i=0;
	for ( i=0;i<b-1 ;i+=1 )
	{
		if(pb[i] == pb[i+1]){
			allDui += 1;
			i++;
		}
	}
	for ( i=0;i<t-1 ;i+=1 )
	{
		if(pt[i] == pt[i+1]){
			allDui += 1;
			i++;
		}

	}
	for ( i=0;i<w-1 ;i+=1 )
	{
		if(pw[i] == pw[i+1]){
			allDui += 1;
			i++;
		}
	}
}

void Group( char *pp,int n)
{
	char q[14];
	char r; 
	int i,j,k=0;
	r = '0';
	for (i = 0;i < n;i++)
	{ 
		q[i] = *(pp + i);
	}
	if (flagDui==0)
	{
		for (i=0 ; i<n-1 ;i+=1 )
		{
			if(q[i] == q[i+1]){
				currentDui1 += 1;
				i++;
			}
			if(currentDui1 > currentDui2){
				currentDui2 +=1;
				flagDui = 1;
				score +=2;
				currentDui1 = 0;
				if (i==n-2)
				{
					n-=2;
					break;
				}
				else {
					for(j=i;j<n-2;j++)
						q[j] = q[j+2];
					n-=2;
					break;
				}
			}
		}
	}
	
	if (n == 0)
	{
		
	}
	else{
		Group3Shunzi(q,n);

	}//输了		
}

void cpares(char * Cards)
{
	char pt[14],pw[14],pb[14],pp[14];
	char temp;
	int t=0,b=0,w=0,k = 0;
	int i,j=0,dd=0;
	for (i=0; i<28; i++)
	{
		if(*(Cards + i) == 'd')
		{
			pb[b++] = *(Cards + i -1); 
		}

		if(*(Cards + i) == 't')
		{
			pt[t++] = *(Cards + i -1); 
		}

		if(*(Cards + i) == 'w')
		{
			pw[w++] = *(Cards + i -1);  
		}
	}
	if(b != 0 && t !=0 && w != 0)
	{
		printf("error\n");
	}
	sort(pb,b);
	sort(pt,t);
	sort(pw,w);
	
	calDui(pb,b,pt,t,pw,w);

	while(currentDui2 < allDui)
	{
		Group(pt,t);
		Group(pw,w);
		Group(pb,b);
		flagDui = 0;
		if(score > oldscore)
			oldscore = score;
		score = 0;
	}
	Group3Shunzi(pt,t);
	Group3Shunzi(pw,w);
	Group3Shunzi(pb,b);
	if(score > oldscore)
		oldscore = score;
	printf("alldui: %d\n",allDui);
	printf("current: %d\n",currentDui2);
	printf("score: %d\n", oldscore);
}


int main()
{
	char tes[30] = {0};
	while(1){
	allDui = 0;
	currentDui2=0;
	currentDui1=0;
	oldscore = 0;
	score =0;
	flagDui=0;
	scanf("%s",tes);
	char *as  = "1D2W2W2D3D4D4D5D5D5D6D6D6D7D";
	char *as1 = "1W1W2T2D3W3W5W5W7W7W8W8W9W9W"; 
	char *as2 = "1W1W1W2W3W4W4W5W6W7W8W9W9W9W";
	cpares(tes);}			//输入了三组测试用例
	printf("press any keys to continue\n");
	getchar();
	return 0;
}

