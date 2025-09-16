# Google Maps URL 格式規範

## ✅ 正確格式

使用 Google Maps Search API 格式：
```
https://www.google.com/maps/search/?api=1&query=Location+Name+Full+Address
```

## 📝 格式規則

1. **基礎 URL**: 必須使用 `https://www.google.com/maps/search/?api=1&query=`
2. **地點名稱**: 包含完整地點名稱
3. **地址**: 包含完整地址
4. **空格處理**: 所有空格用 `+` 替代
5. **符號處理**: 移除逗號和括號
6. **語言**: 使用英文地址格式

## 🎯 正確範例

```markdown
https://www.google.com/maps/search/?api=1&query=Tokyo+Tower+4-2-8+Shibakoen+Minato+City+Tokyo+Japan
https://www.google.com/maps/search/?api=1&query=Senso-ji+Temple+2-3-1+Asakusa+Taito+City+Tokyo+Japan
https://www.google.com/maps/search/?api=1&query=Shibuya+Crossing+Shibuya+City+Tokyo+Japan
```

## ❌ 錯誤格式

**不要使用以下格式：**
- `https://goo.gl/maps/xyz` (短網址)
- `https://maps.google.com/maps?q=` (舊格式)
- `https://www.google.com/maps/place/` (地點格式)
- 包含逗號的查詢參數

## 🔧 URL 產生流程

1. 取得地點名稱和完整地址
2. 合併為：`地點名稱 + 空格 + 完整地址`
3. 所有空格替換為 `+`
4. 移除逗號、括號等符號
5. 加上基礎 URL 前綴

## 📱 測試方法

生成 URL 後，點擊確認：
- ✅ 能正確開啟 Google Maps
- ✅ 顯示正確地點
- ✅ 提供導航功能
- ❌ 不會導向錯誤頁面