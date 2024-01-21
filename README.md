# Anatomy of the Memory Stack

<div class="gp gq ow"><picture><source srcset="https://miro.medium.com/v2/resize:fit:640/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 640w, https://miro.medium.com/v2/resize:fit:720/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 720w, https://miro.medium.com/v2/resize:fit:750/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 750w, https://miro.medium.com/v2/resize:fit:786/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 786w, https://miro.medium.com/v2/resize:fit:828/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 828w, https://miro.medium.com/v2/resize:fit:1100/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 1100w, https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EwdZs-6vDz_u52vNy7mxEg.png 1400w" sizes="(min-resolution: 4dppx) and (max-width: 700px) 50vw, (-webkit-min-device-pixel-ratio: 4) and (max-width: 700px) 50vw, (min-resolution: 3dppx) and (max-width: 700px) 67vw, (-webkit-min-device-pixel-ratio: 3) and (max-width: 700px) 65vw, (min-resolution: 2.5dppx) and (max-width: 700px) 80vw, (-webkit-min-device-pixel-ratio: 2.5) and (max-width: 700px) 80vw, (min-resolution: 2dppx) and (max-width: 700px) 100vw, (-webkit-min-device-pixel-ratio: 2) and (max-width: 700px) 100vw, 700px" type="image/webp"><source data-testid="og" srcset="https://miro.medium.com/v2/resize:fit:640/1*EwdZs-6vDz_u52vNy7mxEg.png 640w, https://miro.medium.com/v2/resize:fit:720/1*EwdZs-6vDz_u52vNy7mxEg.png 720w, https://miro.medium.com/v2/resize:fit:750/1*EwdZs-6vDz_u52vNy7mxEg.png 750w, https://miro.medium.com/v2/resize:fit:786/1*EwdZs-6vDz_u52vNy7mxEg.png 786w, https://miro.medium.com/v2/resize:fit:828/1*EwdZs-6vDz_u52vNy7mxEg.png 828w, https://miro.medium.com/v2/resize:fit:1100/1*EwdZs-6vDz_u52vNy7mxEg.png 1100w, https://miro.medium.com/v2/resize:fit:1400/1*EwdZs-6vDz_u52vNy7mxEg.png 1400w" sizes="(min-resolution: 4dppx) and (max-width: 700px) 50vw, (-webkit-min-device-pixel-ratio: 4) and (max-width: 700px) 50vw, (min-resolution: 3dppx) and (max-width: 700px) 67vw, (-webkit-min-device-pixel-ratio: 3) and (max-width: 700px) 65vw, (min-resolution: 2.5dppx) and (max-width: 700px) 80vw, (-webkit-min-device-pixel-ratio: 2.5) and (max-width: 700px) 80vw, (min-resolution: 2dppx) and (max-width: 700px) 100vw, (-webkit-min-device-pixel-ratio: 2) and (max-width: 700px) 100vw, 700px"><img alt="" class="bg hc hd c" width="700" height="350" loading="lazy" role="presentation" src="https://miro.medium.com/v2/resize:fit:875/1*EwdZs-6vDz_u52vNy7mxEg.png"></picture></div>
<p><ul class=""><li id="527a" class="mv mw hg mx b my mz na nb nc nd ne nf ng nh ni nj nk nl nm nn no np nq nr ns pc pd pe bj" data-selectable-paragraph=""><strong class="mx hh">Extended Stack Pointer (or the ESP):</strong> ESP is the CPU register that points to the top of the memory stack. It may hold the memory address of the instruction being executed or the data that is currently at the top of the memory stack. The value in the ESP changes as the program execution follows.</li><li id="552c" class="mv mw hg mx b my pf na nb nc pg ne nf ng ph ni nj nk pi nm nn no pj nq nr ns pc pd pe bj" data-selectable-paragraph=""><strong class="mx hh">Buffer Space:</strong> It is the space that is allocated to the program for its execution. Generally, the information in the buffer should not be allowed to escape the buffer space. This is done by implementing proper input sanitizations and following a secure coding approach.</li><li id="f8b3" class="mv mw hg mx b my pf na nb nc pg ne nf ng ph ni nj nk pi nm nn no pj nq nr ns pc pd pe bj" data-selectable-paragraph=""><strong class="mx hh">Extended Base Pointer (or the EBP):</strong> EBP is the CPU register that holds the memory address of the top of the stack. This generally remains fixed during the entire program execution and is used as a reference address for the next instructions.</li><li id="dddc" class="mv mw hg mx b my pf na nb nc pg ne nf ng ph ni nj nk pi nm nn no pj nq nr ns pc pd pe bj" data-selectable-paragraph=""><strong class="mx hh">Extended Instruction Pointer (or the EIP):</strong> EIP controls the flow of execution. It holds the location of the next instruction to be executed by the CPU. EIP is the main target of the buffer overflow attack, as controlling the EIP gives the attacker the control of command execution.</li></ul>

# Steps of Buffer Overflow Attack
<p>1) Fuzzing the application to determine the crashing of the application.
<p>2) Finding the exact location of the crash (called the offset).
<p>3) Finding the offset.
<p>4)	Control over the flow of execution by Overwriting the Instruction Pointer (EIP).
<p>5) Checking for bad characters.
<p>6) Finding the Right with no memory protections.
<p>7) Generating ShellCode and gaining access to the target.</p>
<h1 id="df15" class="nt nu hg be nv nw nx ny nz oa ob oc od oe of og oh oi oj ok ol om on oo op oq bj" data-selectable-paragraph="">Defense &amp; Mitigation</h1>
<ul class=""><li id="f07b" class="mv mw hg mx b my or na nb nc os ne nf ng ot ni nj nk ou nm nn no ov nq nr ns pc pd pe bj" data-selectable-paragraph="">Implement secure coding practices when developing and building applications, by using secure programming functions.</li><li id="5103" class="mv mw hg mx b my pf na nb nc pg ne nf ng ph ni nj nk pi nm nn no pj nq nr ns pc pd pe bj" data-selectable-paragraph="">Apply proper input validations and sanitizations.</li><li id="4630" class="mv mw hg mx b my pf na nb nc pg ne nf ng ph ni nj nk pi nm nn no pj nq nr ns pc pd pe bj" data-selectable-paragraph="">Implement memory protections like Address Space Layout Randomization (ASLR), Data Execution Prevention (DEP), Structured Exception Handling (SEH).</li></ul>
