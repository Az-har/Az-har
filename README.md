<div align="center">

# Hi there, I'm Azhar 👋

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=680&lines=Data+Engineer+%7C+Celonis+Process+Mining%3BOrder-to-Cash+(O2C)+Intelligence%3BDatabricks+%26+Modern+Data+Pipelines%3BAutonomous+AI+%26+Local+Agentic+Systems)](https://git.io/typing-svg)

<p align="center">
  <b>Data Engineer</b> specializing in <b>Celonis Process Mining</b>, high-throughput enterprise pipelines, and autonomous applied AI systems.
</p>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/az-har-ayyash/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:azharayyash999@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Az-har)

</div>

---

### 📐 End-to-End Enterprise Data & Process Architecture

```mermaid
flowchart LR
    subgraph INGEST ["1. ERP & Telemetry Ingestion"]
        direction TB
        SAP["SAP ERP (VBAK, VBAP, LIKP, LIPS)"]
        EXT["Live Weather & Disruption Feeds"]
    end

    subgraph PROCESS ["2. Celonis Process Intelligence"]
        direction TB
        EMS["Celonis EMS Event Logs"]
        PQL["PQL Root-Cause & Rework Metrics"]
        AE["Action Engine Auto Write-Backs"]
    end

    subgraph PLATFORMS ["3. Lakehouse & Applied AI"]
        direction TB
        DB["Databricks Master Pipeline"]
        ML["Engine A: Delay Predictor (XGBoost)"]
        RAG["Engine B: SLA & Policy RAG (ChromaDB)"]
    end

    subgraph OUTCOME ["4. Operational Impact"]
        direction TB
        DSO["Reduced DSO & Billing Disputes"]
        SLA["Proactive SLA Breach Mitigation ($)"]
    end

    SAP --> EMS
    EMS --> PQL --> AE
    SAP --> DB
    EXT --> DB
    DB --> ML --> SLA
    DB --> RAG --> DSO
```

---

### 📦 Process Engineering & Capabilities

<table>
  <tr>
    <td width="33%" valign="top">
      <h4>🔍 Celonis & Process Mining</h4>
      <ul>
        <li><b>Process Discovery</b>: Event-log transformation across SAP <code>VBAK</code>, <code>VBAP</code>, <code>LIKP</code>, <code>LIPS</code>.</li>
        <li><b>Advanced PQL</b>: Process cycle time, throughput bottlenecks, and rework rate calculation.</li>
        <li><b>Execution Automation</b>: Action Engine triggers & automated ERP write-backs.</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h4>🏗️ Modern Data Engineering</h4>
      <ul>
        <li><b>Lakehouse Architecture</b>: Databricks master jobs, Spark batch transforms, environmental memory caching.</li>
        <li><b>Modern Data Stack</b>: Dimensional star-schema modeling using <b>dbt</b> & <b>DuckDB</b>.</li>
        <li><b>Data Platforms</b>: Snowflake, PostgreSQL, SQLite WAL concurrency.</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h4>🤖 Autonomous Applied AI</h4>
      <ul>
        <li><b>Process AI</b>: Dual ML delay forecasting + ChromaDB semantic SLA retrieval.</li>
        <li><b>Acoustic Engine</b>: AMD GPU Vulkan Whisper <code>large-v3</code> speech perception.</li>
        <li><b>Critic Loops</b>: Self-evaluating multi-agent LLM verification pipelines.</li>
      </ul>
    </td>
  </tr>
</table>

---

### 🌟 Production Flagships

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center"><a href="https://github.com/Az-har/O2C_AI">🚀 O2C_AI</a></h3>
      <p align="center">
        <a href="https://github.com/Az-har/O2C_AI"><img src="https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white" alt="Databricks" /></a>
        <a href="https://github.com/Az-har/O2C_AI"><img src="https://img.shields.io/badge/Celonis-PQL%20%7C%20O2C-2563EB?style=flat-square" alt="Celonis" /></a>
        <a href="https://github.com/Az-har/O2C_AI"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /></a>
        <a href="https://github.com/Az-har/O2C_AI"><img src="https://img.shields.io/badge/RAG%20%26%20ML-00A4EF?style=flat-square" alt="RAG" /></a>
      </p>
      <p><strong>Enterprise Order-to-Cash (O2C) Process Intelligence &amp; Delay Risk Engine</strong></p>
      <ul>
        <li><strong>Dual AI Architecture</strong>: Mathematical delay prediction on SAP tables coupled with ChromaDB semantic contract &amp; SLA retrieval.</li>
        <li><strong>Financial Exposure</strong>: Translates late delivery risks into exact contractual dollar ($) penalties.</li>
        <li><strong>Databricks Pipeline</strong>: Production batch scoring with vectorized inference and automated ML model validation.</li>
      </ul>
      <p align="center">
        <a href="https://github.com/Az-har/O2C_AI"><strong>Explore O2C_AI &rarr;</strong></a>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center"><a href="https://github.com/Az-har/youtube-summarizer-audiobook">🎧 YouTube Summarizer &amp; Audiobook AI</a></h3>
      <p align="center">
        <a href="https://github.com/Az-har/youtube-summarizer-audiobook"><img src="https://img.shields.io/badge/Whisper-large--v3-000000?style=flat-square&logo=openai&logoColor=white" alt="Whisper" /></a>
        <a href="https://github.com/Az-har/youtube-summarizer-audiobook"><img src="https://img.shields.io/badge/AMD_Vulkan-ED1C24?style=flat-square&logo=amd&logoColor=white" alt="AMD Vulkan" /></a>
        <a href="https://github.com/Az-har/youtube-summarizer-audiobook"><img src="https://img.shields.io/badge/Ollama-Local_LLM-000000?style=flat-square" alt="Ollama" /></a>
        <a href="https://github.com/Az-har/youtube-summarizer-audiobook"><img src="https://img.shields.io/badge/Audio-EBU_R128-00599C?style=flat-square" alt="Audio" /></a>
      </p>
      <p><strong>Autonomous 5-Agent Media Ingestion &amp; Audio Mastering Pipeline</strong></p>
      <ul>
        <li><strong>Acoustic Perception</strong>: Hardware-accelerated Whisper <code>large-v3</code> on AMD GPUs via Vulkan compute with Silero VAD neural pre-filtering.</li>
        <li><strong>Self-Evaluating Critic Loop</strong>: Autonomous multi-turn LLM judge auditing factual consistency, narrative flow, and ad purging.</li>
        <li><strong>Broadcast Mastering</strong>: Studio-grade audio normalization to <strong>EBU R128 (-16 LUFS)</strong> with ID3v2 chapter embedding.</li>
      </ul>
      <p align="center">
        <a href="https://github.com/Az-har/youtube-summarizer-audiobook"><strong>Explore Audiobook AI &rarr;</strong></a>
      </p>
    </td>
  </tr>
</table>

---

### 📂 Additional Engineering Repositories

- **[automotive-analytics-project](https://github.com/Az-har/automotive-analytics-project)**: Modern analytics engineering pipeline transforming raw automotive datasets into multi-tier dimensional marts using **dbt**, **DuckDB**, and **SQL**.
- **[scratchpad-python](https://github.com/Az-har/scratchpad-python)**: Curated standalone Python tools, 3D mathematical terminal graphics (`donut.py`), and CLI utilities.

---

### 🛠️ Technical Skills

<p align="center">
  <img src="https://img.shields.io/badge/Celonis-EMS%20%7C%20PQL-2563EB?style=for-the-badge" alt="Celonis" />
  <img src="https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white" alt="Databricks" />
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" alt="Spark" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQL-CC292B?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL" />
  <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" alt="dbt" />
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB" />
  <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" alt="Snowflake" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

---

### 📊 GitHub Activity & Metrics

<div align="center">
  <img src="https://github-stats-alpha.vercel.app/api?username=Az-har&theme=tokyonight&show_icons=true&hide_border=true" alt="Azhar's GitHub Stats" width="49%" />
  <img src="https://streak-stats.demolab.com/?user=Az-har&theme=tokyonight&hide_border=true" alt="GitHub Streak" width="49%" />
</div>

---

<div align="center">
  <sub>Designed & engineered by <b>Azhar</b> • Powered by Celonis Process Mining, Data Engineering, and Applied AI</sub>
</div>
