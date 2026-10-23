// Simulated service responses only. This never submits an email or customer inquiry.
import vm from 'node:vm';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const code=fs.readFileSync(new URL('../assets/js/inquiry.js',import.meta.url),'utf8');
for (const scenario of ['accepted','rejected-200','http-error','invalid-json','network-error']) {
  const button={disabled:false,textContent:''}, error={hidden:true}, success={style:{display:'none'}};
  const product={value:''};
  const form={action:'https://example.invalid/no-send',style:{display:''},reportValidity:()=>true,querySelector:()=>button};
  const events=[];
  const context=vm.createContext({URLSearchParams,AbortController,setTimeout,clearTimeout,FormData:class {},
    window:{location:{search:'?product=Unlisted%20crab'},clarity:(...args)=>events.push(args)},
    document:{getElementById:id=>({'inquiry-form':form,'form-error':error,'form-success':success,product}[id])},
    fetch:async()=>{
      if(scenario==='network-error')throw new Error('offline');
      return {ok:scenario!=='http-error',json:async()=>{
        if(scenario==='invalid-json')throw new Error('bad json');
        return {success:scenario==='accepted'?'true':false};
      }};
    }});
  vm.runInContext(code,context);
  await context.handleSubmit({preventDefault(){}});
  assert.equal(product.value,'Unlisted crab');
  assert.equal(button.disabled,false);
  assert.equal(success.style.display==='block',scenario==='accepted');
  assert.equal(error.hidden,scenario==='accepted');
  assert.equal(events[0][1],scenario==='accepted'?'inquiry_form_accepted':'inquiry_form_error');
}
console.log('Passed five inquiry response scenarios and free-text product prefill; no network messages sent.');
