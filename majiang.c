
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<sys/time.h>
#include<string.h>
int score = 0;
int oldscore = 0;
int currentDui1 = 0;
int currentDui2 = 0;
int allDui = 0;
int flagDui = 0;
int currentUser=0;
int spool2size=0;

int ptdesk[9]={0};
int pwdesk[9]={0};
int pddesk[9]={0};


typedef struct user1{
	char name;	
	int score;
	char ding;
	int waitPeng;
	int wait[7];
	int ptdesk[9];
	int pwdesk[9];
	int pddesk[9];
	char havePeng[10];
} user;

user u[4];

typedef struct smart1{
	char pai[2];
	int score;
	int num;
} smart;

void showPai(user *u, char pai[]){
	int i,len=0,j;
	for(i=0; i<27; i++){
		if(i<9){
			if(u->ptdesk[i]>0)
				for(j=0; j<u->ptdesk[i]; j++){
					pai[len++]=i+1+48;
					pai[len++]='t';
				}
		}
		else if(i<18){
			if(u->pwdesk[i-9]>0)
				for(j=0; j<u->pwdesk[i-9]; j++){
					pai[len++]=i-9+1+48;
					pai[len++]='w';
				}
		}
		else if(i<27){
			if(u->pddesk[i-18]>0)
				for(j=0; j<u->pddesk[i-18]; j++){
					pai[len++]=i-18+1+48;
					pai[len++]='d';
				}
		}
	}
}


void getPai(user *u, char pai[])
{
	switch(pai[1]){
		case 't':
			(u->ptdesk[pai[0]-48-1])++;
			break;
		case 'w':
			(u->pwdesk[pai[0]-48-1])++;
			break;
		case 'd':
			(u->pddesk[pai[0]-48-1])++;
			break;
	}
}

void putPai(user *u,char pai[]){
	switch(pai[1]){
		case 't':
			(u->ptdesk[pai[0]-48-1])--;
			break;
		case 'w':
			(u->pwdesk[pai[0]-48-1])--;
			break;
		case 'd':
			(u->pddesk[pai[0]-48-1])--;
			break;
	}

}

void printInfo(char tes[],user *u,int *score,int *num);
void smartPut(user *u,char pai[]){
	int i,size=0;
	switch(u->ding){
		case 't':
			for(i=0;i<9;i++)
			{
				if(u->ptdesk[i]!=0)
				{
					pai[0]=i+48+1;
					pai[1]='t';
					return;
				}
			}
			break;
		case 'w':
			for(i=0;i<9;i++)
			{
				if(u->pwdesk[i]!=0)
				{
					pai[0]=i+48+1;
					pai[1]='w';
					return;
				}
			}
			break;
		case 'd':
			for(i=0;i<9;i++)
			{
				if(u->pddesk[i]!=0)
				{
					pai[0]=i+48+1;
					pai[1]='d';
					return;
				}
			}
			break;
	}	
	

	char allPai[30]={0};
	showPai(u,allPai);
	for(i=0;i<15;i++){
		if(allPai[i*2]==0)
		{
			size=i;
			break;
		}
	}
	int maxscore=0,maxnum=0;
	smart overview[14];
	

	for(i=0;i<size;i++)
	{
		int myscore=0,mynum=0;
		char tempPai[30]={0};
		putPai(u,&allPai[i*2]);
		showPai(u,tempPai);
		//printf("%s\n",tempPai);
		printInfo(tempPai,u,&myscore,&mynum);
		overview[i].pai[0]=allPai[i*2];
		overview[i].pai[1]=allPai[i*2+1];
		overview[i].score=myscore;
		overview[i].num=mynum;
		getPai(u,&allPai[i*2]);	
	}
	
	for(i=0;i<size;i++)
	{
		printf("pai:%c%c score:%d num:%d\n",overview[i].pai[0],overview[i].pai[1],overview[i].score,overview[i].num);
	}
	
	for(i=0;i<size;i++)
	{
		if(overview[i].score==maxscore)
			{
				if(overview[i].num>=maxnum){
				maxnum=overview[i].num;
				pai[0]=overview[i].pai[0];
				pai[1]=overview[i].pai[1];
				}
			}
		else if(overview[i].score>maxscore)
			{
				maxscore=overview[i].score;
				
				maxnum=overview[i].num;
				pai[0]=overview[i].pai[0];
				pai[1]=overview[i].pai[1];
				
			}
	}
	//printf("%c%c\n",pai[0],pai[1]);

}

typedef struct info1
{
	char name[2];
	int tempscore;
	int num;
} info; 

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
	char tem[20],*q,*w;

	int i,j,k,m,l,sp = 0;
	m=0;
	for(i=0;i<n;i++){
		tem[i]=p[i];
	}
	q = tem;
	w = q;
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
				i++;
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

int cpares(char * Cards,user *u)
{
	char pt[14],pw[14],pd[14],pp[14];
	char temp;
	int t=0,b=0,w=0,k = 0;
	int i,j=0,dd=0;
	score = 0;
	oldscore = 0;
	currentDui2 = 0;
	currentDui1 = 0;
		
	allDui = 0;
	flagDui = 0;
	int canpeng=0;
	int noduiscore=0;
	
	for (i=0; i<28; i++)
	{
		if(*(Cards + i) == 'd')
		{
			pd[b++] = *(Cards + i -1); 
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
		//printf("error\n");
		return 0;
	}
	sort(pd,b);
	sort(pt,t);
	sort(pw,w);
	
	calDui(pd,b,pt,t,pw,w);

	Group3Shunzi(pt,t);
	Group3Shunzi(pw,w);
	Group3Shunzi(pd,b);
	noduiscore=score;
	if(score > oldscore)
		oldscore = score;
	score=0;
	while(currentDui2 < allDui)
	{
		Group(pt,t);
		Group(pw,w);
		Group(pd,b);
		flagDui = 0;
		if(score > noduiscore)
		{
			canpeng++;
	
		}
		if(score > oldscore)
			oldscore = score;
		score = 0;
	}
	
	//printf("alldui: %d\n",allDui);
	//printf("current: %d\n",currentDui2);
	//printf("score: %d\n", oldscore);
	if(canpeng>0)
	return oldscore+canpeng-1+(u->havePeng[8]-48)*3;
	else
	return oldscore+(u->havePeng[8]-48)*3;
}


int cpares2(char * Cards,user *u)
{
	char pt[14],pw[14],pd[14],pp[14];
	char temp;
	int t=0,b=0,w=0,k = 0;
	int i,j=0,dd=0;
	score = 0;
	oldscore = 0;
	currentDui2 = 0;
	currentDui1 = 0;
		
	allDui = 0;
	flagDui = 0;
	int canpeng=0;
	int noduiscore=0;
	if(u->waitPeng==1){
		memset(u->wait,0,7);
	}
	for (i=0; i<28; i++)
	{
		if(*(Cards + i) == 'd')
		{
			pd[b++] = *(Cards + i -1); 
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
	switch(u->ding)
	{
		case 't':
			t=0;
			break;
		case 'd':
			b=0;
			break;
		case 'w':
			w=0;
			break;
	}
	sort(pd,b);
	sort(pt,t);
	sort(pw,w);
	
	calDui(pd,b,pt,t,pw,w);

	Group3Shunzi(pt,t);
	Group3Shunzi(pw,w);
	Group3Shunzi(pd,b);
	noduiscore=score;
	if(score > oldscore)
		oldscore = score;
	score=0;
	while(currentDui2 < allDui)
	{
		Group(pt,t);
		Group(pw,w);
		Group(pd,b);
		flagDui = 0;
		if(score > noduiscore)
		{
			canpeng++;
			if(u->waitPeng==1)
			{
				u->wait[currentDui2-1]=1;
			}
	
		}
		if(score > oldscore)
			oldscore = score;
		score = 0;
	}
	
	//printf("alldui: %d\n",allDui);
	//printf("current: %d\n",currentDui2);
	//printf("score: %d\n", oldscore);
	if(canpeng>0)
	return oldscore+canpeng-1;
	else
	return oldscore;
}




void printInfo(char tes[],user *u,int *myscore,int *mynum){
	char tes2[30];
	info array[18];
	int i;
	for (i=0;i<30 ;i++ )
	{
		tes2[i]=tes[i];
	}
	char ding=u->ding;
	

	for (i=0;i<9 ;i++ )
	{
		
		switch(ding){
			case 't':
				tes2[26]=i+1+48;
				tes2[27]='d';
				array[i].name[0]=i+1+48;
				array[i].name[1]='d';
				array[i].tempscore=cpares(tes2,u);
				array[i].num=4;//-pddesk[i]-u->pddesk[i];
				break;
			case 'd':
				tes2[26]=i+1+48;
				tes2[27]='t';
				array[i].name[0]=i+1+48;
				array[i].name[1]='t';
				array[i].tempscore=cpares(tes2,u);
				array[i].num=4;//-ptdesk[i]-u->ptdesk[i];
				break;
				
			case 'w':
				tes2[26]=i+1+48;
				tes2[27]='d';
				array[i].name[0]=i+1+48;
				array[i].name[1]='d';
				array[i].tempscore=cpares(tes2,u);
				array[i].num=4;//-pddesk[i]-u->pddesk[i];
				break;
		}
	}



	for (i=0;i<9 ;i++ )
	{
		
		
		switch(ding){
			case 't':
				tes2[26]=i+1+48;
				tes2[27]='w';
				array[i+9].name[0]=i+1+48;
				array[i+9].name[1]='w';
				array[i+9].tempscore=cpares(tes2,u);
				array[i+9].num=4;//-pwdesk[i]-u->pwdesk[i];	
				break;
			case 'd':
				tes2[26]=i+1+48;
				tes2[27]='w';
				array[i+9].name[0]=i+1+48;
				array[i+9].name[1]='w';
				array[i+9].tempscore=cpares(tes2,u);
				array[i+9].num=4;//-pwdesk[i]-u->pwdesk[i];
				break;
			case 'w':
				tes2[26]=i+1+48;
				tes2[27]='t';
				array[i+9].name[0]=i+1+48;
				array[i+9].name[1]='t';
				array[i+9].tempscore=cpares(tes2,u);
				array[i+9].num=4;//-ptdesk[i]-u->ptdesk[i];
				break;
		}
	}
	
	int maxscore=0;
	int totalnum=0;
	for (i=0;i<18 ;i++ )
	{	
		if(array[i].num!=0&&array[i].tempscore>maxscore)
			maxscore=array[i].tempscore;
	}
	for (i=0;i<18 ;i++ )
	{
		if(array[i].tempscore==maxscore){
			/*printf("need:%c%c num:%d score:%d\n",array[i].name[0],array[i].name[1],array[i].num,array[i].tempscore);*/
			totalnum+=array[i].num;
		}
	}
	//printf("totalnum:%d\n",totalnum);
	*myscore=maxscore;
	*mynum=totalnum;
	//printf("%d  %d",maxscore,totalnum);

}
void deskAdd(char pai[]){
	switch(pai[1]){
		case 't':
			ptdesk[pai[0]-48-1]++;
			break;
		case 'w':
			pwdesk[pai[0]-48-1]++;
			break;
		case 'd':
			pddesk[pai[0]-48-1]++;
			break;
	}
}
void spoolInit(char spool1[]){
	struct timeval tpstart;
	float size=108.0;
	int i=0,j=0,n,i2;
	char tempSpool[218]={0};
	for(i=0;i<27;i++)
	{
		for(j=0;j<4;j++){
		if(i<9){
		tempSpool[i*8+j*2]=i+1+48;
		tempSpool[i*8+j*2+1]='w';
		}
		else if(i<18){
		tempSpool[i*8+j*2]=i-9+1+48;
		tempSpool[i*8+j*2+1]='d';	
		}
		else if(i<27){
		tempSpool[i*8+j*2]=i-18+1+48;
		tempSpool[i*8+j*2+1]='t';	
		}
		}
	}
	//printf("tempspool:%s\n",tempSpool);
	for(i=0;i<108;i++){
		gettimeofday(&tpstart,NULL);
		srand(tpstart.tv_usec);
		n=(0+(int)(size*rand()/(RAND_MAX+1.0)));
		spool1[i*2]=tempSpool[n*2];
		spool1[i*2+1]=tempSpool[n*2+1];
		if(n==(int)(size-1)){
			tempSpool[n*2]='\0';
			tempSpool[n*2+1]='\0';
			size=size-1;
		}else{
			for(i2=n*2; i2<(int)(size)*2-2; i2++)
				tempSpool[i2]=tempSpool[i2+2];
			size=size-1;
		}
	}
	

}
void peng(user *u,char p[],int *howmany,int *allmany){
	int i,temp=0,temp2=0;
	if(u->ding!='t')
	for(i=0;i<9;i++)
	{
		if(u->ptdesk[i]>=2&&u->ptdesk[i]<4){
			if(u->wait[temp2]==1){
				p[temp*2]=i+48+1;
				p[temp*2+1]='t';
				temp++;
			}
			temp2++;
		}else if(u->ptdesk[i]==4){
			temp2+=2;
		}
		
	}
	if(u->ding!='w')
	for(i=0;i<9;i++)
	{
		if(u->pwdesk[i]>=2&&u->pwdesk[i]<4){
			if(u->wait[temp2]==1){
				p[temp*2]=i+48+1;
				p[temp*2+1]='w';
				temp++;
			}
			temp2++;
		}else if(u->pwdesk[i]==4){
			temp2+=2;
		}
		
	}
	if(u->ding!='d')
	for(i=0;i<9;i++)
	{
		if(u->pddesk[i]>=2&&u->pddesk[i]<4){
			if(u->wait[temp2]==1){
				p[temp*2]=i+48+1;
				p[temp*2+1]='d';
				temp++;
			}
			temp2++;
		}else if(u->pddesk[i]==4){
			temp2+=2;
		}
		
	}
	*howmany=temp;
	*allmany=temp2;
}
int doPeng(int u2,char pai[], char spool2[]){
	int i,j,howmany,allmany,have=-1;
	char temp[2]={0};
	char temp2[30]={0};
	char temp3[30]={0};
	char tempPeng[14]={0};
	char peng1[14]={0};
	for(i=0;i<4;i++){
		if(i!=u2){
			memset(tempPeng,0,14);
			peng(&u[i],tempPeng,&howmany,&allmany);
			for(j=0;j<7;j++){
				if(tempPeng[j*2]==pai[0]&&tempPeng[j*2+1]==pai[1]){
					have=i;
					break;
				}					
			}
		}
	}
	if(have!=-1){
		currentUser=have;
		int havePeng=0;
		u[currentUser].waitPeng=0;
		showPai(&u[currentUser],temp2);
		havePeng=u[currentUser].havePeng[8]-48;
		u[currentUser].havePeng[havePeng*2]=pai[0];
		u[currentUser].havePeng[havePeng*2+1]=pai[1];
		u[currentUser].havePeng[8]=havePeng+1+48;
		putPai(&u[currentUser],&pai[0]);
		putPai(&u[currentUser],&pai[0]);
		showPai(&u[currentUser],temp3);
		printf("User:u%d  Pai:%s  Peng:%c%c  Ding:%c  Score:%d  Score2:%d  have:%d\n",currentUser,temp2,pai[0],pai[1],u[currentUser].ding,cpares(temp2,&u[currentUser]),cpares(temp3,&u[currentUser]),u[currentUser].havePeng[8]-48);
		smartPut(&u[currentUser],temp);
		putPai(&u[currentUser],temp);
		spool2[(spool2size)*2]=temp[0];
		spool2[(spool2size)*2+1]=temp[1];
		spool2size++;
		deskAdd(&temp[0]);
		memset(temp2,0,30);
		showPai(&u[currentUser],temp2);
		u[currentUser].waitPeng=1;
		cpares2(temp2,&u[currentUser]);
		
		peng(&u[currentUser],peng1,&howmany,&allmany);
			
		printf("User:u%d  Pai:%s  Da:%c%c  Score:%d  peng:%s  num:%d all:%d\n",currentUser,temp2,temp[0],temp[1],cpares(temp2,&u[currentUser]),peng1,howmany,allmany);
		printf("Dsk:%s \n",spool2);
		getchar();
		doPeng(currentUser,temp,spool2);
	}else
		return 0;
}



void sureDing(user *u){
	int i,j,pt=0,pw=0,pd=0,temp=15;
	for(i=0;i<9;i++){
		pt=pt+u->ptdesk[i];
		pw=pw+u->pwdesk[i];
		pd=pd+u->pddesk[i];
	}
	if(pt<temp){
		temp=pt;
		u->ding='t';
	}
	if(pw<temp){
		temp=pw;
		u->ding='w';
	}
	if(pd<temp){
		temp=pd;
		u->ding='d';
	}
}
int main()
{
	
	int i;
	char pai[2]={0};
	char tes[30] = {0};
	char tes2[30] ={0};
	char spool1[218]={0};
	
	char spool2[218]={0};
	int  peng2=0;
	
	spoolInit(spool1);

	
	for(i=0;i<4;i++){
		memset(u[i].ptdesk,0,9*sizeof(int));
		memset(u[i].pddesk,0,9*sizeof(int));
		memset(u[i].pwdesk,0,9*sizeof(int));
		u[i].waitPeng=0;
		u[i].havePeng[8]='0';
		u[i].havePeng[9]='\0';
	}
	for(i=0;i<52;i++){
		if(i<13)
			getPai(&u[0],&spool1[i*2]);
		else if(i<26)
			getPai(&u[1],&spool1[i*2]);
		else if(i<39)
			getPai(&u[2],&spool1[i*2]);
		else if(i<52)
			getPai(&u[3],&spool1[i*2]);
	}
	
	for(i=0;i<4;i++){
		memset(tes,0,30);
		showPai(&u[i],tes);
		sureDing(&u[i]);
		printf("u%d:%s ding:%c\n",i,tes,u[i].ding);
	}
	
	for(i=52;i<108;i++)
	{
		char temp[2]={0};
		char temp2[30]={0};
	
		char temp3[30]={0};
		char peng1[14]={0};
		
		int howmany=0;
		int allmany=0;
		
		u[currentUser].waitPeng=0;
		showPai(&u[currentUser],temp2);
		
		getPai(&u[currentUser],&spool1[i*2]);
		showPai(&u[currentUser],temp3);
		printf("User:u%d  Pai:%s  Mo:%c%c  Ding:%c  Score:%d  Score2:%d have:%d\n",currentUser,temp2,spool1[i*2],spool1[i*2+1],u[currentUser].ding,cpares(temp2,&u[currentUser]),cpares(temp3,&u[currentUser]),u[currentUser].havePeng[8]-48);

		if(u[currentUser].ding==spool1[i*2+1]){
			putPai(&u[currentUser],&spool1[i*2]);
			spool2[(spool2size)*2]=spool1[i*2];
			spool2[(spool2size)*2+1]=spool1[i*2+1];
			spool2size++;
			deskAdd(&spool1[i*2]);
			memset(temp2,0,30);
			showPai(&u[currentUser],temp2);
			u[currentUser].waitPeng=1;
			cpares2(temp2,&u[currentUser]);
			peng(&u[currentUser],peng1,&howmany,&allmany);
			
			printf("User:u%d  Pai:%s  Da:%c%c  Score:%d  peng:%s  num:%d all:%d\n",currentUser,temp2,spool1[i*2],spool1[i*2+1],cpares(temp2,&u[currentUser]),peng1,howmany,allmany);
			printf("Dsk:%s \n",spool2);
			getchar();

			doPeng(currentUser,&spool1[i*2],spool2);

			currentUser=(currentUser+1)%4;
		
			continue;
		}
		smartPut(&u[currentUser],temp);
		putPai(&u[currentUser],temp);
		spool2[(spool2size)*2]=temp[0];
		spool2[(spool2size)*2+1]=temp[1];
		spool2size++;
		deskAdd(&temp[0]);
		memset(temp2,0,30);
		showPai(&u[currentUser],temp2);
		u[currentUser].waitPeng=1;
		cpares2(temp2,&u[currentUser]);
		peng(&u[currentUser],peng1,&howmany,&allmany);
		printf("User:u%d  Pai:%s  Da:%c%c  Score:%d  peng:%s  num:%d all:%d\n",currentUser,temp2,temp[0],temp[1],cpares(temp2,&u[currentUser]),peng1,howmany,allmany);
		printf("Dsk:%s \n",spool2);
		getchar();
		doPeng(currentUser,temp,spool2);
		currentUser=(currentUser+1)%4;

	}
	/*
	int i;
	char tes[30];
	char pai[2];
	scanf("%s",tes);
	user u0;
	memset(u0.ptdesk,0,9*sizeof(int));
	memset(u0.pddesk,0,9*sizeof(int));
	memset(u0.pwdesk,0,9*sizeof(int));
	for(i=0;i<14;i++){
		getPai(&u0,&tes[i*2]);
	}
	
	smartPut(&u0,pai);*/
	/*
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
	cpares(tes);}	
			//输入了三组测试用例



	scanf("%s %c",tes,&ding);
	printInfo(tes,ding);
	printf("press any keys to continue\n");
	getchar();*/
	return 0;
	
}

