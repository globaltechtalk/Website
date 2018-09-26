import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ContactComponent } from './contact/contact.component';
import { SponsersComponent } from './sponsers/sponsers.component';
import { CommunityPartnerComponent } from './community-partner/community-partner.component';
import { TeamComponent } from './team/team.component';

const routes: Routes = [
  { path: 'contact', component: ContactComponent },
  { path: 'sponsers', component: SponsersComponent },
  { path: 'commu', component: CommunityPartnerComponent },
  { path: 'team', component: TeamComponent },
];

@NgModule({
  imports: [
    CommonModule, RouterModule.forRoot(routes)
  ],
  exports: [ RouterModule ],
  declarations: []
})
export class AppRoutingModule { }
// export const routingComponents = [ContactComponent]
