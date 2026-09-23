package com.reachpilot.ai
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

data class Trend(val title:String,val platform:String,val signal:String,val relevance:String,val reason:String)
val demoTrends=listOf(
 Trend("OMR / ECR Chennai Vibes","Instagram","Rising fast","High","Travel, beach and Chennai lifestyle format"),
 Trend("Tamil Trending Audio","Instagram","Rising","High","Audio-led Tamil short-form content"),
 Trend("Tamil Tech Reviews","YouTube","Rising","High","Search-led Tamil technology content"),
 Trend("Best Restaurants in Chennai","Google","High interest","High","Local search opportunity"))
val purple=Color(0xFF8B5CF6); val bg=Color(0xFF080B18); val card=Color(0xFF12182B)

class MainActivity:ComponentActivity(){override fun onCreate(b:Bundle?){super.onCreate(b);setContent{ReachPilotApp()}}}

@Composable fun ReachPilotApp(){
 var tab by remember{mutableStateOf("Home")}; var selected by remember{mutableStateOf<Trend?>(null)}
 MaterialTheme(colorScheme=darkColorScheme(primary=purple,background=bg,surface=card)){
  Scaffold(containerColor=bg,bottomBar={NavigationBar(containerColor=Color(0xFF0D1222)){listOf("Home","Platforms","Create","Analytics","Profile").forEach{n->NavigationBarItem(selected=tab==n,onClick={tab=n;selected=null},icon={Icon(when(n){"Home"->Icons.Default.Home;"Platforms"->Icons.Default.GridView;"Create"->Icons.Default.AddCircle;"Analytics"->Icons.Default.ShowChart;else->Icons.Default.Person},n)},label={Text(n)})}}}){p->
   Box(Modifier.padding(p)){val s=selected;if(s!=null)TrendDetail(s){selected=null}else when(tab){"Platforms"->Platforms();"Create"->CreateAI();"Analytics"->Analytics();else->Home{selected=it}}}
  }
 }
}
@Composable fun Header(title:String,sub:String){Column{Text(title,color=Color.White,fontSize=28.sp,fontWeight=FontWeight.Bold);Text(sub,color=Color(0xFFAAB3CC),fontSize=14.sp)}}
@Composable fun Home(open:(Trend)->Unit){LazyColumn(Modifier.fillMaxSize().padding(20.dp),verticalArrangement=Arrangement.spacedBy(14.dp)){item{Header("Good evening 👋","AI growth intelligence for creators")};item{Text("Chennai ▾",color=Color.White,fontWeight=FontWeight.SemiBold)};item{Card(colors=CardDefaults.cardColors(containerColor=Color(0xFF18234A)),shape=RoundedCornerShape(18.dp)){Column(Modifier.padding(18.dp)){Text("12 fresh opportunities",color=Color.White,fontSize=19.sp,fontWeight=FontWeight.Bold);Text("Across Instagram, YouTube, Google and more",color=Color(0xFFB8C1DB));Spacer(Modifier.height(10.dp));Button(onClick={}){Text("View all")}}}};item{Text("Top opportunities today",color=Color.White,fontSize=20.sp,fontWeight=FontWeight.Bold)};items(demoTrends){x->TrendCard(x){open(x)}}}}
@Composable fun TrendCard(x:Trend,click:()->Unit){Card(Modifier.fillMaxWidth().clickable{click()},colors=CardDefaults.cardColors(containerColor=card),shape=RoundedCornerShape(18.dp)){Column(Modifier.padding(16.dp)){Row(Modifier.fillMaxWidth(),horizontalArrangement=Arrangement.SpaceBetween){Text(x.platform,color=Color(0xFFB9A7FF));Text(x.signal,color=Color(0xFF5EE6A8),fontWeight=FontWeight.Bold)};Spacer(Modifier.height(7.dp));Text(x.title,color=Color.White,fontSize=18.sp,fontWeight=FontWeight.Bold);Text("Chennai relevance: "+x.relevance,color=Color(0xFFB7C0D8));Text(x.reason,color=Color(0xFF8893AF),fontSize=13.sp)}}}
@Composable fun Platforms(){LazyColumn(Modifier.padding(20.dp),verticalArrangement=Arrangement.spacedBy(12.dp)){item{Header("Choose platform","Platform-specific trends, tools and AI")};items(listOf("Instagram · Reels, audio, formats","YouTube · Videos, Shorts, SEO","Facebook · Reels, posts, pages","Google · Trends, SEO, keywords","LinkedIn · Professional growth","Pinterest · Visual search","X · Real-time conversations","WhatsApp Business · Campaigns","Website / Blog · SEO & content")){x->Card(colors=CardDefaults.cardColors(containerColor=card)){Text(x,Modifier.fillMaxWidth().padding(20.dp),color=Color.White,fontWeight=FontWeight.SemiBold)}}}}
@Composable fun TrendDetail(x:Trend,back:()->Unit){LazyColumn(Modifier.padding(20.dp),verticalArrangement=Arrangement.spacedBy(14.dp)){item{IconButton(onClick=back){Icon(Icons.Default.ArrowBack,"Back",tint=Color.White)}};item{Text(x.platform,color=Color(0xFFB9A7FF));Header(x.title,x.signal+" · Chennai relevance "+x.relevance)};item{Card(colors=CardDefaults.cardColors(containerColor=card)){Column(Modifier.padding(18.dp)){Text("Why it's trending",color=Color.White,fontSize=19.sp,fontWeight=FontWeight.Bold);Text("• Increasing topic activity\n• Cross-platform confirmation can strengthen confidence\n• Creator relevance is personalized\n• Evidence must be source-backed",color=Color(0xFFB7C0D8))}}};item{Text("Trend Content Explorer",color=Color.White,fontSize=20.sp,fontWeight=FontWeight.Bold);Text("Top · Latest · Fastest Growing · Tamil · Chennai · Small Creators",color=Color(0xFFAAB3CC))};items(listOf("Discoverable reels / videos","AI pattern analysis","Content gaps & opportunities")){z->Card(colors=CardDefaults.cardColors(containerColor=card)){Text(z,Modifier.fillMaxWidth().padding(18.dp),color=Color.White)}};item{Button(onClick={},modifier=Modifier.fillMaxWidth()){Text("Create content for this trend")}}}}
@Composable fun CreateAI(){LazyColumn(Modifier.padding(20.dp),verticalArrangement=Arrangement.spacedBy(12.dp)){item{Header("Create with AI","Turn an opportunity into original content")};items(listOf("1  Idea & angle","2  Hook (first 3 seconds)","3  Script · 15 / 30 / 60 sec","4  Shot list & storyboard","5  Caption","6  SEO & hashtags","7  Thumbnail concept","8  Pre-publish check")){x->Card(colors=CardDefaults.cardColors(containerColor=card)){Text(x,Modifier.fillMaxWidth().padding(18.dp),color=Color.White)}};item{Button(onClick={},modifier=Modifier.fillMaxWidth()){Text("Start creating")}}}}
@Composable fun Analytics(){LazyColumn(Modifier.padding(20.dp),verticalArrangement=Arrangement.spacedBy(14.dp)){item{Header("Growth intelligence","Connected-account analytics & AI coach")};items(listOf("Views & reach","Watch time / retention","Shares & saves","Top performing content","Creator DNA","What worked?","What to improve?","Next best actions")){x->Card(colors=CardDefaults.cardColors(containerColor=card)){Text(x,Modifier.fillMaxWidth().padding(18.dp),color=Color.White)}}}}
