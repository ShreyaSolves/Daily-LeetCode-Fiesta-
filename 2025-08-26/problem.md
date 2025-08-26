# 🧩 Daily LeetCode Challenge: Two Sum

Yo, welcome to **Day 2** of our daily coding vibe! ✨ Today, we’re diving into the **Two Sum** problem (Easy) from LeetCode—a super chill way to flex those coding muscles. This guide’s got the lowdown on the problem, a fun and simple solution, and why it went smooth as butter. No hiccups today, just pure **Shreya-style** coding joy! 💻🌸 Perfect for anyone ready to crush this with a smile.

---

## 📌 Problem

You get a list of numbers (`nums`, like `[2, 7, 11, 15]`) and a target number (`target`, like `9`). Your job: find **two numbers** in the list that add up to the target and return their positions (like `[0, 1]` since `2 + 7 = 9`). 

✅ There’s exactly one answer.  
✅ Can’t pick the same spot twice.  
✅ Order of indices doesn’t matter.  
✅ Bonus: Can you skip the slow O(n²) way of checking every pair?

---

## ✨ Examples

**Example 1**  
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
textWhy? `2 + 7 = 9`, so `nums[0] + nums[1]` hits the target.

**Example 2**  
Input: nums = [3,2,4], target = 6  
Output: [1,2]  
textWhy? `2 + 4 = 6`, so `nums[1] + nums[2]`.

**Example 3**  
Input: nums = [3,3], target = 6  
Output: [0,1]  
textWhy? `3 + 3 = 6`, so `nums[0] + nums[1]`.

---

## ⚡ Constraints

- `2 ≤ nums.length ≤ 10⁴` (2 to 10,000 numbers)  
- `-10⁹ ≤ nums[i], target ≤ 10⁹` (big or negative numbers)  
- Exactly one solution exists  
- No reusing the same index  
- **Follow-up**: Beat O(n²) time  

---

## 🛠️ Solution

Today was like a sunny day with zero clouds—everything just *clicked*! 🌞 We used a **hash map** (our magic notebook 📒) to make this lightning-fast, hitting that sweet O(n) vibe. Think of it like finding two snacks that perfectly split your pizza bill. Instead of trying every combo (snooze), we jot down numbers in a notebook and check for their match as we go.

### How it works:
1. Start with an empty notebook (`num_to_index`).  
2. Stroll through the list, one number at a time.  
3. For each number, find its perfect match (`target - num`).  
4. Check the notebook: Is the match there?  
   - Yup? Boom, return its index and the current one. 🎯  
   - Nope? Add the number and its spot to the notebook, keep rolling.  
5. One solution’s guaranteed, so we’ll find it!

## 💭 Reflections  

Day 2 was a total vibe check—nailed it first try! 😎  
The hash map was like picking the perfect song on the first shuffle: quick, smooth, no repeats.  
We crushed the **O(n)** goal, and those test cases lit up green like a neon sign.  
This problem’s a reminder that a smart tool (like our notebook) can make coding feel like a breeze.  

Can’t wait to keep the streak going on **Day 3! 🚀**  

---

## 📬 Contact  

- **GitHub**: [ShreyaSolves](https://github.com/ShreyaSolves)  
- **Email**: shreyamanibu@gmail.com  

---

✨ Happy coding, y’all! Keep the vibes high and the bugs low.  
Catch you at the next challenge! 🌟
