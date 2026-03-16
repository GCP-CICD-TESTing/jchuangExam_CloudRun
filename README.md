# This project is develop mode!!

This project is aims to exam the CI/CD process of cloud run.

### 分支架構說明
- **`prod` 分支**：正式穩定版本。此分支受保護，**僅接受從 `val` 分支發起的 Pull Request**，不接受直接推送或其他分支的合併。
- **`val` 分支 (預設)**：開發與驗證分支。這是所有開發者的主要工作場域，也是 PR 的預設目標。所有的功能更新都必須先在這裡經過測試與驗證。

### 提交貢獻

1. **Fork 或 Clone 專案**：
   - 請直接下載 `val`分支
     ```bash
     git clone -b val --single-branch https://github.com/GCP-CICD-TESTing/jchuangExam_CloudRun.git
     ```
2. **建立功能分支**：
   - 請從 `val` 分支切出新分支進行開發：
     ```bash
     cd jchuangExam_CloudRun
     git checkout -b feature/your-feature-name
     ```
3. **提交修改並推送**：
   - 完成開發後，將分支推送到遠端：
     ```bash
     git push origin feature/your-feature-name
     ```
4. **發起 Pull Request (PR)**：
   - 建立 PR 時，請確保 **Base 分支選擇 `val`**。
   - 經過審核與測試通過後，你的代碼將會合併進 `val`。

### 注意事項
- 請勿直接push程式碼到`val` OR `prod`
- 請勿直接向 `prod` 分支發起 PR，否則系統會自動攔截或拒絕。
- 所有的代碼在進入 `prod` 之前，都必須先在 `val` 分支中運行正常。