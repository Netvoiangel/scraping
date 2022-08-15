import {
  Subjects,
  Publisher,
  ExpirationCompleteEvent,
} from "@wrstickets/common";

export class ExpirationCompletePublisher extends Publisher<ExpirationCompleteEvent> {
  subject: Subjects.ExpirationComplete = Subjects.ExpirationComplete;
}
