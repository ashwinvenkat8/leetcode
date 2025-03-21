# leetdump

- [Python](#python)
- [Zsh](#zsh-script)
- [Limitations](#limitations-of-the-zsh-script)

> [!NOTE]
> You can find my accepted solutions [here](https://github.com/ashwinvenkat8/leetdump/tree/main/src). I will try to keep it updated.

Recently, I wanted to get all the solutions I submitted on Leetcode as I wanted to share them with a few people.
My first thought was to look for an export option in Leetcode as I assumed this was a common need. While there is a page to
[view all submissions](https://leetcode.com/submissions/), you need to visit each problem to view and store your solution offline.

Next, I searched online for automated solutions and there are many with varying complexity. But being an engineer
myself, I decided to build one that suits my current requirement. Now that I've built it, I wanted to share it so you can modify and use it as needed.

> [!CAUTION]
> My implementation does not handle rate limiting as I did not need it. Feel free to handle that in your implementation.
> You can either set a fixed timeout before retrying or use a more dynamic solution like exponential backoff.

## Python

[This script](https://github.com/ashwinvenkat8/leetdump/blob/main/leetdump.py) will fetch all submissions from an account and write them as files to a specified output directory. Currently, Python (`.py`), Java (`.java`), JavaScript (`.js`), and PostgreSQL (`.sql`) code will be written with their correct extensions. Any other type of code will be written as `.txt`.

## Zsh Script

[This script](https://github.com/ashwinvenkat8/leetdump/blob/main/leetdump.sh) was the first one I developed to get my submissions. Once this executed, I had some manual work before it was ready to be stored as files. It was fun developing this as I don't use Zsh scripts often.

## Limitations of the Zsh Script

- Figuring out the total number of submissions requires manual effort - _run the curl command with different offsets till
you get a null/empty response_. In my case, that offset was 240. Alternatively, you can spend some time changing the script
to a while loop that fetches submissions till a null/empty response is encountered.

- The `limit` query parameter is hardcoded in my script since Leetcode has capped it at 20. Higher values did not work but
feel free to test for your own sanity.

- The response from the _submissions_ API is a JSON array. So, my current implementation is to append '---' after each
response. This makes it easier for me to join the data into a single array once the script completes execution.
Joining the data is another manual step (which was faster for me at the time) but this is simple to implement in code.

I hope this helps you. Thank you for reading!
