import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, BarChart3, Brain, Crown, Gauge, Layers3, Megaphone, Network, ShieldCheck, TrendingDown, Users, Zap } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Cell, Line, LineChart, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import './styles.css';

const pages = ['Overview', 'Churn Lab', 'Segments', 'Campaigns', 'Revenue Risk', 'Operations'];
const churnTrend = [
  { month: 'Jan', churn: 8.2, saved: 1.1 }, { month: 'Feb', churn: 7.7, saved: 1.4 }, { month: 'Mar', churn: 7.1, saved: 1.8 },
  { month: 'Apr', churn: 6.8, saved: 2.2 }, { month: 'May', churn: 6.1, saved: 2.9 }, { month: 'Jun', churn: 5.6, saved: 3.4 }
];
const segments = [
  { name: 'Premium Streamers', value: 31, color: '#38bdf8' }, { name: 'Price Sensitive', value: 24, color: '#f59e0b' },
  { name: 'Roaming Heavy', value: 18, color: '#a78bfa' }, { name: 'Dormant Prepaid', value: 27, color: '#fb7185' }
];
const revenue = [
  { region: 'North', arpu: 18.4, risk: 5.2 }, { region: 'South', arpu: 13.7, risk: 8.9 }, { region: 'East', arpu: 15.1, risk: 6.4 }, { region: 'West', arpu: 20.2, risk: 4.1 }
];
const customers = [
  ['C-90018','Premium Streamers','82%','High','Unlimited 5G retention bundle'],
  ['C-90221','Price Sensitive','68%','Medium','Discounted family add-on'],
  ['C-90442','Roaming Heavy','73%','High','Travel data pack renewal'],
  ['C-90991','Dormant Prepaid','57%','Medium','Recharge cashback campaign']
];

function predictFallback(form){
  let risk = 18;
  const reasons = [];
  if (Number(form.monthly_charges) > 60) { risk += 18; reasons.push('High monthly bill pressure'); }
  if (Number(form.tenure_months) < 8) { risk += 20; reasons.push('New customer with weak loyalty history'); }
  if (Number(form.support_tickets) > 3) { risk += 18; reasons.push('Repeated support friction'); }
  if (form.contract_type === 'month_to_month') { risk += 22; reasons.push('Month-to-month contract increases churn mobility'); }
  risk = Math.min(risk, 96);
  return { churn_probability: risk / 100, risk_band: risk > 75 ? 'critical' : risk > 60 ? 'high' : risk > 35 ? 'medium' : 'low', segment: 'Price Sensitive', recommended_action: risk > 60 ? 'Trigger retention offer and supervisor follow-up' : 'Enroll in next-best-offer campaign', reasons };
}

function App(){
  const [active, setActive] = useState('Overview');
  const [form, setForm] = useState({ monthly_charges: 72, tenure_months: 5, support_tickets: 4, contract_type: 'month_to_month' });
  const [insight, setInsight] = useState(predictFallback(form));
  const metrics = useMemo(() => [
    ['Customers Monitored','2.4M','+14.8%',Users], ['Predicted Churn','5.6%','-2.6 pts',TrendingDown], ['Revenue Protected','$8.7M','+21%',Crown], ['Campaign Lift','17.9%','+4.2%',Zap]
  ], []);
  const runInsight = async () => {
    try {
      const response = await fetch('/customers/insights', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(form) });
      if (!response.ok) throw new Error('offline');
      setInsight(await response.json());
    } catch { setInsight(predictFallback(form)); }
  };
  return <main className="app-shell">
    <aside className="sidebar"><div className="brand"><Network/><div><strong>TelcoPulse AI</strong><span>Customer Intelligence Cloud</span></div></div>{pages.map(page => <button className={active===page?'active':''} onClick={()=>setActive(page)} key={page}>{page}</button>)}</aside>
    <section className="workspace"><header className="topbar"><div><p className="eyebrow">Telecom retention command center</p><h1>{active}</h1></div><button onClick={runInsight}>Run customer insight</button></header>
      {active==='Overview' && <Overview metrics={metrics}/>} {active==='Churn Lab' && <ChurnLab form={form} setForm={setForm} insight={insight} runInsight={runInsight}/>} {active==='Segments' && <Segments/>} {active==='Campaigns' && <Campaigns/>} {active==='Revenue Risk' && <RevenueRisk/>} {active==='Operations' && <Operations/>}
    </section>
  </main>;
}

function Overview({metrics}){return <><section className="metrics">{metrics.map(([label,value,delta,Icon])=><article className="card" key={label}><Icon/><span>{label}</span><strong>{value}</strong><small>{delta}</small></article>)}</section><section className="grid"><Panel title="Churn trend" icon={<Activity/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={churnTrend}><CartesianGrid strokeDasharray="3 3" stroke="#1f3750"/><XAxis dataKey="month" stroke="#8da2b8"/><YAxis stroke="#8da2b8"/><Tooltip/><Area type="monotone" dataKey="churn" stroke="#38bdf8" fill="#0e7490"/><Area type="monotone" dataKey="saved" stroke="#22c55e" fill="#166534"/></AreaChart></ResponsiveContainer></Panel><Panel title="Segment mix" icon={<Layers3/>}><ResponsiveContainer width="100%" height={260}><PieChart><Pie data={segments} dataKey="value" nameKey="name" outerRadius={95}>{segments.map(s=><Cell key={s.name} fill={s.color}/>)}</Pie><Tooltip/></PieChart></ResponsiveContainer></Panel></section></>}
function ChurnLab({form,setForm,insight,runInsight}){return <section className="grid"><Panel title="Customer risk simulator" icon={<Brain/>}>{Object.entries(form).map(([k,v])=><label key={k}>{k.replaceAll('_',' ')}<input value={v} onChange={e=>setForm({...form,[k]:e.target.value})}/></label>)}<button onClick={runInsight}>Predict churn</button></Panel><Panel title="Prediction result" icon={<Gauge/>}><div className="score"><span className={insight.risk_band}>{insight.risk_band}</span><strong>{Math.round(insight.churn_probability*100)}%</strong><p>{insight.recommended_action}</p></div>{(insight.reasons||[]).map(r=><div className="reason" key={r}>{r}</div>)}</Panel></section>}
function Segments(){return <section className="grid"><Panel title="Customer segments" icon={<Layers3/>}><div className="segment-list">{segments.map(s=><div className="segment" key={s.name}><span style={{background:s.color}}></span><strong>{s.name}</strong><small>{s.value}% of base</small></div>)}</div></Panel><Panel title="Priority customers" icon={<Users/>}><Table rows={customers}/></Panel></section>}
function Campaigns(){return <section className="grid"><Panel title="Retention campaign studio" icon={<Megaphone/>}><div className="playbook"><h3>Next best actions</h3><p>Auto-build offers based on churn drivers, ARPU, and segment behavior.</p><button>Generate offer plan</button></div></Panel><Panel title="Campaign lift forecast" icon={<BarChart3/>}><ResponsiveContainer width="100%" height={260}><BarChart data={revenue}><XAxis dataKey="region" stroke="#8da2b8"/><YAxis stroke="#8da2b8"/><Tooltip/><Bar dataKey="arpu" fill="#38bdf8"/><Bar dataKey="risk" fill="#f97316"/></BarChart></ResponsiveContainer></Panel></section>}
function RevenueRisk(){return <section className="grid"><Panel title="Regional revenue exposure" icon={<Crown/>}><ResponsiveContainer width="100%" height={260}><LineChart data={revenue}><XAxis dataKey="region" stroke="#8da2b8"/><YAxis stroke="#8da2b8"/><Tooltip/><Line dataKey="arpu" stroke="#22c55e" strokeWidth={3}/><Line dataKey="risk" stroke="#fb7185" strokeWidth={3}/></LineChart></ResponsiveContainer></Panel><Panel title="Leakage alerts" icon={<ShieldCheck/>}><div className="reason">South region price-sensitive churn projected above threshold.</div><div className="reason">Roaming Heavy segment has renewal drop-off risk in 14 days.</div><div className="reason">Dormant prepaid base requires recharge campaign intervention.</div></Panel></section>}
function Operations(){return <section className="grid"><Panel title="Model operations" icon={<Gauge/>}><div className="ops"><b>Model version:</b> telco-churn-v1.4<br/><b>Drift status:</b> Stable<br/><b>Batch scoring:</b> 2.4M customers/day<br/><b>SLA:</b> 99.95%</div></Panel><Panel title="Team workflow" icon={<Activity/>}><div className="reason">Retention team reviews high-risk customers daily at 09:00.</div><div className="reason">Campaign outcomes sync to analytics warehouse every 6 hours.</div><div className="reason">Executive revenue summary generated weekly.</div></Panel></section>}
function Panel({title,icon,children}){return <article className="panel"><div className="panel-title">{icon}<h2>{title}</h2></div>{children}</article>}
function Table({rows}){return <div className="table">{rows.map(row=><div className="row" key={row[0]}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div>}

createRoot(document.getElementById('root')).render(<App/>);
